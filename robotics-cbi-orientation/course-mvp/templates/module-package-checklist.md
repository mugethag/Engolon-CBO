# Module Package Checklist

Use this checklist for every new module. Module 1 and Module 2 are the reference packages.

Reference examples:

- `term-1/module-1/`
- `term-1/module-2/`

## Required Files

Create a folder for the module:

```text
term-X/module-Y/
  lesson-script.md
  storyboard.md
  quiz.md
  handout.md
```

## Lesson Script Standard

The lesson script should include:

- Module title
- Estimated video duration
- Scene 1: Title
- Scene 2: Learning Outcomes
- Scene 3: Core Concept 1
- Scene 4: Core Concept 2
- Scene 5: Applied Example
- Scene 6: Checkpoint
- Scene 7: Recap

Writing rules:

- Use direct learner-facing narration.
- Keep technical detail accurate but introductory unless the module requires depth.
- Use examples connected to robotics, drones, environment, infrastructure, cybersecurity, or intelligent systems.
- Avoid operationally harmful drone or cyber instructions.

## Storyboard Standard

The storyboard should include:

- Target video duration
- Scene table with time, purpose, and visual direction
- Reusable scene notes
- Any simulation, diagram, or animation requirements

## Quiz Standard

Each quiz should include:

- 10 questions minimum
- Four answer options per question
- Answer key
- Outcome mapping
- Feedback-ready wording where possible

Question types:

- Concept identification
- Scenario reasoning
- Vocabulary
- Risk or ethics judgment
- Applied interpretation

## Handout Standard

Each handout should include:

- Big Idea
- Core Terms
- Process or system diagram in text/table form
- Checklist or memory aid
- Reflection prompt

## Video Production Standard

Before producing the HyperFrames video:

- Confirm script and storyboard are approved.
- Reuse visual identity from `../../DESIGN.md`.
- Keep on-screen text brief.
- Use narration for detail.
- Run `npm run check`.
- Render draft MP4.
- Review for readability, audio pacing, and caption overlap.
- Render final MP4.

## Moodle Upload Standard

For each module in Moodle:

- Add lesson overview page.
- Upload or embed MP4.
- Add handout as PDF or page.
- Build quiz in Moodle question bank.
- Add checkpoint/reflection activity if needed.
- Mark completion criteria.
- Confirm student role can access the materials.
