# Task Logic Audit

## 1. Paradigm Intent

- Task: classic two-phase, three-choice Mnemonic Similarity Task (MST).
- Primary construct: mnemonic discrimination / pattern separation supported by hippocampal dentate gyrus–CA3 circuitry.
- Manipulated factors: phase (incidental study vs recognition test), test item type (target, lure, foil), and lure similarity bin (L1–L5).
- Dependent measures: Lure Discrimination Index, corrected recognition, response accuracy, response distribution, and reaction time.
- Key citations: SRC001–SRC004.

## 2. Block/Trial Workflow

### Block Structure

- Total blocks: two sequential blocks, one study block followed immediately by one surprise recognition-test block.
- Trials per block: 128 study trials and 192 test trials in the full profile.
- Randomization/counterbalancing: Set 1 contains 192 object pairs. A seeded session plan selects 64 lure pairs balanced across the five empirical similarity bins. Of the remaining pair IDs, 64 become targets and 64 become foils. Study and test orders are independently shuffled.
- Condition weight policy: not applicable; global pairing and non-overlap constraints require a custom generator.
- Condition generation method: custom `generate_mst_session(...)`; simple labels cannot guarantee that a studied `a` image becomes either the identical target or the paired `b` lure while reserving disjoint foil IDs.
- Generated condition shape: scalar `MSTTrialPlan` values carrying phase, condition, pair ID, asset path, lure bin, valid keys, and correct key.
- Runtime-generated trial values: none. All item identity, phase, order, and correct responses are preplanned from the configured session seed.

### Trial State Machine

1. Object judgment / recognition:
   - Onset trigger: phase- and condition-specific image trigger.
   - Stimuli shown: one color photograph of an everyday object on a white background plus a compact phase prompt above it.
   - Valid keys: study `V` (indoor) or `N` (outdoor); test `V` (old), `B` (similar), or `N` (new).
   - Timeout behavior: record no response and emit the phase timeout trigger.
   - Next state: inter-stimulus interval.
2. Inter-stimulus interval:
   - Onset trigger: ISI.
   - Stimuli shown: white blank screen.
   - Valid keys: none.
   - Timeout behavior: fixed 0.5 s.
   - Next state: next trial, phase transition, or task summary.

The object is displayed for 2.0 s and the ISI lasts 0.5 s, matching the official PsychoPy implementation distributed by the Stark Lab and the published classic MST descriptions.

## 3. Condition Semantics

- `study_repeat`: studied `a` exemplar that will reappear identically as a target.
- `study_lure`: studied `a` exemplar whose paired `b` exemplar will appear as a lure.
- `target`: exact repetition of a studied `a` image; correct response is old (`V`).
- `lure`: similar but nonidentical paired `b` image; correct response is similar (`B`).
- `foil`: previously unseen `a` image from a disjoint pair; correct response is new (`N`).
- Participant-facing text source: `config/*.yaml` stimuli.
- Localization strategy: Chinese instructions and prompts use SimHei; the object photographs themselves contain no task labels.

## 4. Response and Scoring Rules

- Response mapping: study `V=室内`, `N=室外`; test `V=旧`, `B=相似`, `N=新`.
- Response key source: config task fields.
- Missing-response policy: record timeout; do not impute a category.
- Correctness logic: test response matches the item class mapping above. Study judgments are incidental and therefore not scored for semantic accuracy because the released stimulus set does not include an authoritative indoor/outdoor key.
- Reward/penalty updates: none.
- Running metrics: response rate and mean RT; final metrics additionally include `LDI=P(Similar|Lure)-P(Similar|Foil)` and `REC=P(Old|Target)-P(Old|Foil)`.

## 5. Stimulus Layout Plan

- Screen name: study object.
- Stimulus IDs shown together: dynamic `object_image` and `study_prompt`.
- Layout anchors: prompt `[0, 6.0]`; image `[0, -0.4]`.
- Size/spacing: image `[10, 10]` deg; prompt height `0.55`, wrap width `24`.
- Readability/overlap checks: prompt is above the image with more than 1 deg clearance.
- Rationale: mirrors the official task's persistent phase question while keeping the object central.

- Screen name: test object.
- Stimulus IDs shown together: dynamic `object_image` and `test_prompt`.
- Layout anchors and sizes: same as the study screen.
- Readability/overlap checks: three response labels remain in one compact line above the image.
- Rationale: identical image geometry across target, lure, and foil trials avoids a condition cue.

## 6. Trigger Plan

- Experiment start/end: 1/99; block start/end: 10/90.
- Study image: 20; study responses V/N: 21/22; study timeout: 23.
- Target/lure/foil images: 30/31/32.
- Test responses old/similar/new: 40/41/42; test timeout: 43.
- ISI: 50.

## 7. Architecture Decisions (Auditability)

- `main.py` runtime flow style: one explicit flow that builds one session plan, runs study, reveals the surprise recognition instructions, then runs test.
- `utils.py` used: yes, solely for the paired-item session generator and summary metrics.
- Custom controller used: no.
- Legacy/backward-compatibility fallback logic required: no.
- Custom generator justification: the globally disjoint target/lure/foil assignment and study-to-test pair linkage cannot be represented by independent label-level scheduling.

## 8. Inference Log

- Decision: use Set 1 from the official Stark Lab repository.
- Why inference was required: the papers describe multiple equivalent sets but do not prescribe a single default.
- Citation-supported rationale: SRC001 states that independently matched stimulus sets are used; the official repository provides the exact paired Set 1 photographs and lure-bin file.

- Decision: preserve the full two-second display and fixed 0.5-second blank ISI, with response collection confined to the object display.
- Why inference was required: the official legacy script can also accept late responses during the ISI.
- Citation-supported rationale: published procedures describe 2.0-second object exposure and 0.5-second ISI; confining responses to the visible-object window produces an auditable modern deadline without changing stimulus timing.
