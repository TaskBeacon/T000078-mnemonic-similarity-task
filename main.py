from __future__ import annotations

from contextlib import nullcontext
from functools import partial
from pathlib import Path
from typing import Any

import pandas as pd
from psychopy import core
from psyflow import (
    BlockUnit,
    StimBank,
    StimUnit,
    SubInfo,
    TaskRunOptions,
    TaskSettings,
    context_from_config,
    initialize_exp,
    initialize_triggers,
    load_config,
    parse_task_run_options,
    runtime_context,
)

from src import generate_mst_session, run_trial, summarize_test

MODES = ("human", "qa", "sim")
DEFAULT_CONFIG_BY_MODE = {
    "human": "config/config.yaml",
    "qa": "config/config_qa.yaml",
    "sim": "config/config_scripted_sim.yaml",
}


def _run_block(
    *,
    name: str,
    index: int,
    plans: list[Any],
    settings: TaskSettings,
    win: Any,
    kb: Any,
    bank: StimBank,
    triggers: Any,
    sink: list[dict[str, Any]],
) -> None:
    (
        BlockUnit(
            block_id=name,
            block_idx=index,
            settings=settings,
            window=win,
            keyboard=kb,
        )
        .add_condition(plans)
        .on_start(lambda _: triggers.send(settings.triggers.get("block_start")))
        .on_end(lambda _: triggers.send(settings.triggers.get("block_end")))
        .run_trial(
            partial(
                run_trial,
                stim_bank=bank,
                trigger_runtime=triggers,
                block_id=name,
                block_idx=index,
            )
        )
        .to_dict(sink)
    )


def run(options: TaskRunOptions) -> None:
    root = Path(__file__).resolve().parent
    config = load_config(str(options.config_path))
    output_dir, scope, context = None, nullcontext(), None
    if options.mode in ("qa", "sim"):
        context = context_from_config(task_dir=root, config=config, mode=options.mode)
        output_dir, scope = context.output_dir, runtime_context(context)

    with scope:
        if options.mode == "qa":
            subject = {"subject_id": "qa"}
        elif options.mode == "sim":
            subject = {"subject_id": str(context.session.participant_id or "sim")}
        else:
            subject = SubInfo(config["subform_config"]).collect()

        settings = TaskSettings.from_dict(config["task_config"])
        settings.add_subinfo(subject)
        if output_dir is not None:
            settings.save_path = str(output_dir)
        if options.mode == "qa" and output_dir is not None:
            output_dir.mkdir(parents=True, exist_ok=True)
            settings.res_file = str(output_dir / "qa_trace.csv")
            settings.log_file = str(output_dir / "qa_psychopy.log")
            settings.json_file = str(output_dir / "qa_settings.json")
        settings.triggers = config["trigger_config"]

        triggers = (
            initialize_triggers(mock=True)
            if options.mode in ("qa", "sim")
            else initialize_triggers(config)
        )
        win, kb = initialize_exp(settings)
        bank = StimBank(win, config["stim_config"]).preload_all()
        settings.save_to_json()

        study_plans, test_plans = generate_mst_session(
            asset_dir=root / "assets" / "objects",
            bin_file=root / "assets" / "set1_bins.tsv",
            items_per_test_condition=int(settings.items_per_test_condition),
            seed=int(settings.random_seed),
        )
        all_rows: list[dict[str, Any]] = []
        triggers.send(settings.triggers.get("experiment_start"))
        StimUnit("study_instruction", win, kb, runtime=triggers).add_stim(
            bank.get("study_instruction")
        ).wait_and_continue()
        _run_block(
            name="study",
            index=0,
            plans=study_plans,
            settings=settings,
            win=win,
            kb=kb,
            bank=bank,
            triggers=triggers,
            sink=all_rows,
        )

        StimUnit("test_instruction", win, kb, runtime=triggers).add_stim(
            bank.get("test_instruction")
        ).wait_and_continue()
        _run_block(
            name="test",
            index=1,
            plans=test_plans,
            settings=settings,
            win=win,
            kb=kb,
            bank=bank,
            triggers=triggers,
            sink=all_rows,
        )

        results = summarize_test(all_rows)
        StimUnit("good_bye", win, kb, runtime=triggers).add_stim(
            bank.get_and_format(
                "good_bye",
                ldi=f"{results['ldi']:.3f}",
                recognition=f"{results['recognition']:.3f}",
                accuracy=f"{results['accuracy']:.1%}",
                response_rate=f"{results['response_rate']:.1%}",
                mean_rt=f"{results['mean_rt']:.3f}",
            )
        ).wait_and_continue(terminate=True)
        triggers.send(settings.triggers.get("experiment_end"))
        pd.DataFrame(all_rows).to_csv(settings.res_file, index=False)
        triggers.close()
        core.quit()


def main() -> None:
    run(
        parse_task_run_options(
            task_root=Path(__file__).resolve().parent,
            description="Run the classic two-phase Mnemonic Similarity Task.",
            default_config_by_mode=DEFAULT_CONFIG_BY_MODE,
            modes=MODES,
        )
    )


if __name__ == "__main__":
    main()
