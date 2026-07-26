# Stimulus Mapping

## Mapping Table

| Condition | Stage/Phase | Stimulus IDs | Participant-Facing Content | Source Paper ID | Evidence (quote/figure/table) | Implementation Mode | Asset References | Notes |
|---|---|---|---|---|---|---|---|---|
| `study_repeat` | study | `object_image`, `study_prompt` | One everyday-object `a` photograph; indoor/outdoor prompt | SRC001 | Traditional MST begins with incidental indoor/outdoor judgments for everyday objects. | licensed_external_asset | `assets/objects/*a.jpg` | Pair is reserved for an exact target. |
| `study_lure` | study | `object_image`, `study_prompt` | One everyday-object `a` photograph; indoor/outdoor prompt | SRC001 | Same incidental encoding phase. | licensed_external_asset | `assets/objects/*a.jpg` | Paired `b` photograph is reserved as a lure. |
| `target` | test | `object_image`, `test_prompt` | Exact repetition of a studied photograph; old/similar/new prompt | SRC001 | One third of test images are exact repetitions. | licensed_external_asset | `assets/objects/*a.jpg` | Correct category: old. |
| `lure` | test | `object_image`, `test_prompt` | Similar but nonidentical paired photograph; old/similar/new prompt | SRC001 | One third are perceptually similar lures, varying across L1–L5. | licensed_external_asset | `assets/objects/*b.jpg`, `assets/set1_bins.tsv` | Correct category: similar. |
| `foil` | test | `object_image`, `test_prompt` | Previously unseen everyday-object photograph; old/similar/new prompt | SRC001 | One third are novel foils. | licensed_external_asset | `assets/objects/*a.jpg` | Correct category: new. |

The photographs and lure-bin file come directly from the official Stark Lab MST repository documented in `source_assets.md`; they are not generic substitutes or placeholders.
