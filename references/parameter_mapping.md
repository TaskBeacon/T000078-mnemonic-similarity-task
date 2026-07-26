# Parameter Mapping

## Mapping Table

| Parameter ID | Config Path | Implemented Value | Source Paper ID | Evidence (quote/figure/table) | Decision Type | Notes |
|---|---|---:|---|---|---|---|
| P01 | `task.items_per_test_condition` | 64 | SRC001 | Traditional two-phase MST uses equal target, lure, and foil thirds. | cited | Produces 128 study and 192 test trials. |
| P02 | `timing.object_duration` | 2.0 s | SRC001 | Classic object photographs are presented for 2 s. | cited | Matches official PsychoPy default. |
| P03 | `timing.isi_duration` | 0.5 s | SRC001 | Classic MST procedures use a 0.5-s inter-stimulus interval. | cited | White blank screen. |
| P04 | `task.old_key` | V | SRC001 | Standard three-choice test requires old/similar/new responses. | inferred | Key identity follows contemporary published implementations; category semantics are canonical. |
| P05 | `task.similar_key` | B | SRC001 | Standard three-choice test requires old/similar/new responses. | inferred | Middle key spatially maps to the middle category. |
| P06 | `task.new_key` | N | SRC001 | Standard three-choice test requires old/similar/new responses. | inferred | Category semantics are canonical. |
| P07 | `task.random_seed` | 78078 | SRC001 | Trial order is randomized. | inferred | Fixed seed enables QA/replay. |
| P08 | session generator | 64 lure pairs balanced over L1–L5 | SRC001 | MST lure pairs span five empirical mnemonic-similarity bins. | cited | Uses official Set 1 bin metadata. |
| P09 | LDI | `P(B|lure)-P(B|foil)` | SRC001 | Review defines LDI as similar responses to lures corrected by similar responses to foils. | cited | Primary outcome. |
| P10 | REC | `P(V|target)-P(V|foil)` | SRC001 | Review describes corrected traditional object recognition. | cited | Secondary outcome. |
