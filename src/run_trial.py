from __future__ import annotations

from typing import Any

from psyflow import StimUnit, next_trial_id, set_trial_context

from .utils import MSTTrialPlan


def run_trial(
    win,
    kb,
    settings,
    condition,
    stim_bank,
    trigger_runtime,
    block_id=None,
    block_idx=None,
):
    if not isinstance(condition, MSTTrialPlan):
        raise TypeError("Mnemonic Similarity Task trials require MSTTrialPlan.")
    plan = condition.to_dict()
    trial_id = int(next_trial_id())
    phase = str(plan["phase"])
    condition_id = str(plan["condition"])
    keys = (
        [str(settings.study_indoor_key), str(settings.study_outdoor_key)]
        if phase == "study"
        else [str(settings.old_key), str(settings.similar_key), str(settings.new_key)]
    )
    correct_key = str(plan["correct_key"])
    duration = float(settings.object_duration)
    data: dict[str, Any] = {
        "trial_id": trial_id,
        "phase": phase,
        "block_id": str(block_id or phase),
        "block_idx": int(block_idx or 0),
        "condition": condition_id,
        "condition_id": condition_id,
        "pair_id": int(plan["pair_id"]),
        "image_member": str(plan["image_member"]),
        "image_path": str(plan["image_path"]),
        "lure_bin": plan["lure_bin"],
        "correct_key": correct_key,
    }
    image_trigger = (
        settings.triggers.get("study_image")
        if phase == "study"
        else settings.triggers.get(condition_id)
    )
    response_trigger = (
        {
            str(settings.study_indoor_key): settings.triggers.get("study_indoor_response"),
            str(settings.study_outdoor_key): settings.triggers.get("study_outdoor_response"),
        }
        if phase == "study"
        else {
            str(settings.old_key): settings.triggers.get("old_response"),
            str(settings.similar_key): settings.triggers.get("similar_response"),
            str(settings.new_key): settings.triggers.get("new_response"),
        }
    )
    unit = (
        StimUnit("object", win, kb, runtime=trigger_runtime)
        .add_stim(stim_bank.rebuild("object_image", image=plan["image_path"]))
        .add_stim(stim_bank.get("study_prompt" if phase == "study" else "test_prompt"))
    )
    set_trial_context(
        unit,
        trial_id=trial_id,
        phase=phase,
        deadline_s=duration,
        valid_keys=keys,
        block_id=str(block_id or phase),
        condition_id=condition_id,
        task_factors={
            "stage": phase,
            "condition": condition_id,
            "pair_id": int(plan["pair_id"]),
            "lure_bin": plan["lure_bin"],
            "correct_key": correct_key,
        },
        stim_id=f"{plan['pair_id']:03d}{plan['image_member']}",
    )
    capture_kwargs: dict[str, Any] = {
        "keys": keys,
        "duration": duration,
        "onset_trigger": image_trigger,
        "response_trigger": response_trigger,
        "timeout_trigger": settings.triggers.get(f"{phase}_timeout"),
        "terminate_on_response": False,
    }
    if phase == "test":
        capture_kwargs["correct_keys"] = [correct_key]
    unit.capture_response(**capture_kwargs).to_dict(data)
    response = unit.get_state("response", None)
    rt = unit.get_state("rt", None)
    data.update(
        response_key=str(response or ""),
        response_rt=float(rt) if isinstance(rt, (int, float)) else None,
        correct=(str(response) == correct_key) if phase == "test" and response else None,
        timed_out=response is None,
    )

    isi_duration = float(settings.isi_duration)
    isi = StimUnit("isi", win, kb, runtime=trigger_runtime).add_stim(
        stim_bank.get("blank")
    )
    set_trial_context(
        isi,
        trial_id=trial_id,
        phase="isi",
        deadline_s=isi_duration,
        valid_keys=[],
        block_id=str(block_id or phase),
        condition_id=condition_id,
        task_factors={"stage": "isi", "condition": condition_id},
        stim_id="blank",
    )
    isi.show(
        duration=isi_duration, onset_trigger=settings.triggers.get("isi")
    ).to_dict(data)
    return data
