from __future__ import annotations

import random as _random
from dataclasses import dataclass
from typing import Any

from psyflow.sim.contracts import Action, Feedback, Observation, SessionInfo


@dataclass
class TaskSamplerResponder:
    test_accuracy: float = 0.85
    timeout_rate: float = 0.02
    rt_s: float = 0.25
    continue_key: str = "space"

    def __post_init__(self) -> None:
        self._rng: Any = None

    def start_session(self, session: SessionInfo, rng: Any) -> None:
        self._rng = rng

    def on_feedback(self, fb: Feedback) -> None:
        return None

    def end_session(self) -> None:
        self._rng = None

    def _draw(self) -> float:
        return float(self._rng.random()) if hasattr(self._rng, "random") else _random.random()

    @staticmethod
    def _factors(obs: Observation) -> dict[str, Any]:
        factors = dict(getattr(obs, "task_factors", {}) or {})
        if not factors and isinstance(getattr(obs, "extras", None), dict):
            factors = dict(obs.extras.get("task_factors", {}) or {})
        return factors

    def act(self, obs: Observation) -> Action:
        keys = [str(key) for key in list(obs.valid_keys or [])]
        if not keys:
            return Action(key=None, rt_s=None, meta={"source": "mst_sampler", "reason": "no_keys"})
        factors = self._factors(obs)
        stage = str(factors.get("stage", getattr(obs, "phase", ""))).lower()
        if any(token in stage for token in ("instruction", "good_bye", "summary")):
            key = self.continue_key if self.continue_key in keys else keys[0]
            return Action(key=key, rt_s=self.rt_s, meta={"source": "mst_sampler", "stage": stage})
        if self._draw() < self.timeout_rate:
            return Action(key=None, rt_s=None, meta={"source": "mst_sampler", "stage": stage, "outcome": "timeout"})
        correct_key = str(factors.get("correct_key", ""))
        if correct_key in keys and self._draw() < self.test_accuracy:
            key, outcome = correct_key, "correct"
        else:
            alternatives = [key for key in keys if key != correct_key]
            key = alternatives[int(self._draw() * len(alternatives)) % len(alternatives)] if alternatives else keys[0]
            outcome = "study_judgment" if not correct_key else "incorrect"
        return Action(key=key, rt_s=self.rt_s, meta={"source": "mst_sampler", "stage": stage, "outcome": outcome})
