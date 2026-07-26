from __future__ import annotations

import csv
import random
from pathlib import Path
from types import MappingProxyType
from typing import Any


class MSTTrialPlan(str):
    """Scalar condition label carrying an immutable preplanned MST item."""

    def __new__(cls, *, condition: str, **payload: Any):
        instance = super().__new__(cls, condition)
        instance._payload = MappingProxyType({"condition": condition, **payload})
        return instance

    def to_dict(self) -> dict[str, Any]:
        return dict(self._payload)


def load_lure_bins(path: Path) -> dict[int, int]:
    bins: dict[int, int] = {}
    with path.open("r", encoding="utf-8", newline="") as stream:
        for row in csv.reader(stream, delimiter="\t"):
            if not row:
                continue
            pair_id, lure_bin = int(row[0]), int(row[1])
            bins[pair_id] = lure_bin
    if set(bins) != set(range(1, 193)):
        raise ValueError("The MST Set 1 lure-bin file must contain pair IDs 1 through 192.")
    if not set(bins.values()).issubset({1, 2, 3, 4, 5}):
        raise ValueError("MST lure bins must be integers from 1 through 5.")
    return bins


def _balanced_lure_ids(
    bins: dict[int, int], count: int, rng: random.Random
) -> list[int]:
    by_bin = {
        lure_bin: [pair_id for pair_id, value in bins.items() if value == lure_bin]
        for lure_bin in range(1, 6)
    }
    for values in by_bin.values():
        rng.shuffle(values)
    selected: list[int] = []
    while len(selected) < count:
        for lure_bin in range(1, 6):
            if by_bin[lure_bin] and len(selected) < count:
                selected.append(by_bin[lure_bin].pop())
    return selected


def generate_mst_session(
    *,
    asset_dir: Path,
    bin_file: Path,
    items_per_test_condition: int,
    seed: int,
) -> tuple[list[MSTTrialPlan], list[MSTTrialPlan]]:
    """Preplan paired study/test items with disjoint target, lure, and foil IDs."""
    count = int(items_per_test_condition)
    if count < 1 or count > 64:
        raise ValueError("items_per_test_condition must be between 1 and 64.")
    bins = load_lure_bins(bin_file)
    rng = random.Random(int(seed))
    lure_ids = _balanced_lure_ids(bins, count, rng)
    remaining = [pair_id for pair_id in range(1, 193) if pair_id not in lure_ids]
    rng.shuffle(remaining)
    foil_ids = remaining[:count]
    target_ids = remaining[count : 2 * count]

    def image_path(pair_id: int, member: str) -> str:
        path = asset_dir / f"{pair_id:03d}{member}.jpg"
        if not path.is_file():
            raise FileNotFoundError(path)
        return str(path.as_posix())

    study: list[MSTTrialPlan] = []
    for pair_id in target_ids:
        study.append(
            MSTTrialPlan(
                condition="study_repeat",
                phase="study",
                pair_id=pair_id,
                image_member="a",
                image_path=image_path(pair_id, "a"),
                lure_bin=None,
                correct_key="",
            )
        )
    for pair_id in lure_ids:
        study.append(
            MSTTrialPlan(
                condition="study_lure",
                phase="study",
                pair_id=pair_id,
                image_member="a",
                image_path=image_path(pair_id, "a"),
                lure_bin=bins[pair_id],
                correct_key="",
            )
        )

    test: list[MSTTrialPlan] = []
    for pair_id in target_ids:
        test.append(
            MSTTrialPlan(
                condition="target",
                phase="test",
                pair_id=pair_id,
                image_member="a",
                image_path=image_path(pair_id, "a"),
                lure_bin=None,
                correct_key="v",
            )
        )
    for pair_id in lure_ids:
        test.append(
            MSTTrialPlan(
                condition="lure",
                phase="test",
                pair_id=pair_id,
                image_member="b",
                image_path=image_path(pair_id, "b"),
                lure_bin=bins[pair_id],
                correct_key="b",
            )
        )
    for pair_id in foil_ids:
        test.append(
            MSTTrialPlan(
                condition="foil",
                phase="test",
                pair_id=pair_id,
                image_member="a",
                image_path=image_path(pair_id, "a"),
                lure_bin=None,
                correct_key="n",
            )
        )
    rng.shuffle(study)
    rng.shuffle(test)
    return study, test


def summarize_test(rows: list[dict[str, Any]]) -> dict[str, float]:
    test_rows = [row for row in rows if row.get("phase") == "test"]

    def rate(response: str, condition: str) -> float:
        items = [row for row in test_rows if row.get("condition") == condition]
        return (
            sum(row.get("response_key") == response for row in items) / len(items)
            if items
            else 0.0
        )

    responded = [row for row in test_rows if row.get("response_key")]
    correct = [row for row in test_rows if bool(row.get("correct"))]
    rts = [
        float(row["response_rt"])
        for row in responded
        if isinstance(row.get("response_rt"), (int, float))
    ]
    return {
        "ldi": rate("b", "lure") - rate("b", "foil"),
        "recognition": rate("v", "target") - rate("v", "foil"),
        "accuracy": len(correct) / len(test_rows) if test_rows else 0.0,
        "response_rate": len(responded) / len(test_rows) if test_rows else 0.0,
        "mean_rt": sum(rts) / len(rts) if rts else 0.0,
    }
