---
name: new-module
description: Scaffold a new robotics certificate course module package (lesson-script, storyboard, quiz, handout) from the Module 1/2 production standard. Invoked as /new-module <number> "<Full Module Title>". Creates all four files and updates COURSE_PRODUCTION_TRACKER.md.
disable-model-invocation: true
---

# new-module skill

Scaffold a complete course module package for the Engolon CBO robotics certificate program.

## Arguments

The user supplies two arguments after `/new-module`:

1. **Module number** — an integer (e.g., `3`)
2. **Module title** — the full title in quotes (e.g., `"Autonomous Systems, Sensor Integration and Swarm Robotics"`)

If either argument is missing, ask the user for it before proceeding.

## Context — read before writing

Read these files to internalize tone, depth, and structure. Do NOT skip this step.

- `robotics-cbi-orientation/course-mvp/term-1/module-1/lesson-script.md`
- `robotics-cbi-orientation/course-mvp/term-1/module-1/storyboard.md`
- `robotics-cbi-orientation/course-mvp/term-1/module-1/quiz.md`
- `robotics-cbi-orientation/course-mvp/term-1/module-1/handout.md`
- `robotics-cbi-orientation/course-mvp/term-1/module-2/lesson-script.md`
- `COURSE_PRODUCTION_TRACKER.md` — for the full module list so you know what comes before and after

## Output directory

`robotics-cbi-orientation/course-mvp/term-1/module-<N>/`

Create it if it does not exist. Write all four files into it.

## File 1 — lesson-script.md

```
# Module <N> Lesson Script

Module title: <Full Module Title>

Estimated video duration: 7-8 minutes

## Scene 1: Title
## Scene 2: Learning Outcomes
## Scene 3: <First core concept>
## Scene 4: <Second core concept>
## Scene 5: <Third core concept>
## Scene 6: <Fourth core concept>
## Scene 7: <Fifth core concept>
## Scene 8: Applied Example
## Scene 9: Checkpoint
## Scene 10: Recap
```

Rules:
- Scenes 3–7 cover the module's distinct technical concepts (adapt count if the topic genuinely needs 4 or 6 — keep total scenes 10).
- Scene 1 (Title): welcome sentence, one-sentence framing of what the module builds on, one sentence on why it matters.
- Scene 2 (Learning Outcomes): state 5 measurable outcomes with "By the end of this module, you should be able to…"
- Scene 8 (Applied Example): ground all concepts in one concrete scenario relevant to East African community or environmental context (water, agriculture, urban infrastructure, wildlife, renewable energy).
- Scene 9 (Checkpoint): one diagnostic question that requires the learner to reason across two or more concepts from this module. Note that there may be more than one defensible answer.
- Scene 10 (Recap): brief summary of the module's main ideas; close with a transition sentence referencing the next module in the tracker.
- Tone: clear, direct, jargon-defined-at-first-use, no unexplained acronyms.
- Length per scene: 80–150 words.

## File 2 — storyboard.md

```
# Module <N> Storyboard

Module: <Full Module Title>

Target video duration: 7-8 minutes

| Scene | Time | Purpose | Visual Direction |
| --- | ---: | --- | --- |
| 1. Title | 0:00-0:30 | ... | ... |
| 2. Learning outcomes | 0:30-1:05 | ... | ... |
| 3. <concept> | 1:05-1:55 | ... | ... |
| 4. <concept> | 1:55-2:50 | ... | ... |
| 5. <concept> | 2:50-3:45 | ... | ... |
| 6. <concept> | 3:45-4:50 | ... | ... |
| 7. <concept> | 4:50-5:40 | ... | ... |
| 8. Applied example | 5:40-6:45 | ... | ... |
| 9. Checkpoint | 6:45-7:15 | ... | ... |
| 10. Recap | 7:15-7:45 | ... | ... |

## Reusable Scene Notes

- Use the same title and outcomes scene style as the orientation video.
- Keep all diagrams simple enough to render in HTML/CSS.
- Avoid hardware-specific claims unless a later SME review confirms them.
- The checkpoint can become an LMS discussion question or embedded quiz prompt.
```

Rules:
- Visual Direction should be specific and implementable in HTML/CSS (diagrams, labeled illustrations, icon sets, split-screen comparisons, animated arrows). No photographic or physical prop references.
- Purpose column: one short phrase.
- Time column: cumulative, 7–8 minutes total; distribute time proportionally to concept complexity.

## File 3 — quiz.md

```
# Module <N> Quiz

Module: <Full Module Title>

Recommended passing score: 70%

## Questions

1. <question>
   - A. ...
   - B. ...
   - C. ...
   - D. ...

[continue for questions 2–10]

## Answer Key

| Question | Answer | Outcome |
| --- | --- | --- |
| 1 | <letter> | <learning outcome tested> |
...
```

Rules:
- 10 questions, each with 4 options (A–D), one correct.
- Exactly one question per learning outcome from Scene 2 (map at least 2 questions to the two most important outcomes).
- Distractors must be plausible but clearly wrong on reflection — no trick questions, no ambiguous wording.
- Outcome column in the answer key: copy the exact outcome phrase from Scene 2 that the question tests.
- Difficulty: introductory undergraduate level; no calculations required.

## File 4 — handout.md

```
# Learner Handout: Module <N>

Module: <Full Module Title>

## Big Idea

[Two-sentence synthesis of the module's central argument]

## Core Terms

| Term | Meaning |
| --- | --- |
[8–12 rows, one per key concept or technical term introduced]

## [Framework section title — e.g., "Key Process", "Decision Checklist", "Design Principles"]

[A numbered list, bullet checklist, or brief framework that gives learners a portable mental model they can apply. 5–8 items. Model after the "Robotics Subsystem Loop" or "Sustainability Design Checklist" in Module 1.]

## Reflection Prompt

[One prompt asking learners to apply the module's ideas to a real situation in their own community or context. One to two sentences.]
```

Rules:
- "Big Idea" is not a summary — it is the module's thesis: what the learner should walk away believing or being able to do differently.
- Core Terms table: define precisely but accessibly, no circular definitions.
- Framework section: give it a title specific to the module topic (not always a "loop" — could be a checklist, a decision tree description, a hierarchy, or a set of design principles).
- Reflection prompt: always anchors to the learner's own community or context, consistent with the East African / Kenya setting of the program.

## Tracker update

After writing all four files, update `COURSE_PRODUCTION_TRACKER.md`:

Find the table row for Module <N>. Set the Script, Storyboard, Quiz, and Handout columns to `Drafted`. Do not change any other column values.

## Completion report

After all files are written and the tracker is updated, output:

```
Module <N> package created:
  robotics-cbi-orientation/course-mvp/term-1/module-<N>/lesson-script.md
  robotics-cbi-orientation/course-mvp/term-1/module-<N>/storyboard.md
  robotics-cbi-orientation/course-mvp/term-1/module-<N>/quiz.md
  robotics-cbi-orientation/course-mvp/term-1/module-<N>/handout.md
  COURSE_PRODUCTION_TRACKER.md updated — Module <N> row set to Drafted.

Next step: SME review of lesson-script.md, then HyperFrames composition.
```
