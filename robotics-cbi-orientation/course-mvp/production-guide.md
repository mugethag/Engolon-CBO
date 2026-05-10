# CBT Production Guide

This guide operationalizes the MVP so future modules can be produced consistently and at lower cost.

Use `../../COURSE_PRODUCTION_TRACKER.md` as the master status tracker for all modules, videos, quizzes, handouts, labs, and Moodle upload work.

## Asset Pattern Per Module

Each module should include:

1. Lesson script
2. Scene-by-scene storyboard
3. HyperFrames video composition
4. Quiz
5. Learner handout
6. Optional simulation or practice activity

## Recommended Video Structure

| Scene | Target Duration | Purpose |
| --- | ---: | --- |
| Title | 15-20s | Establish module topic and relevance |
| Outcomes | 30-45s | State what learners will be able to do |
| Concept 1 | 60-90s | Explain the first core idea |
| Concept 2 | 60-90s | Explain the second core idea |
| Applied Example | 60-90s | Connect concept to robotics, drones, environment, or infrastructure |
| Checkpoint | 20-30s | Ask a short learner reflection or quiz-style prompt |
| Recap | 30-45s | Reinforce main takeaways and bridge to next module |

## HyperFrames Implementation Pattern

- Start from `../index.html`.
- Duplicate the scene structure and replace content.
- Keep `DESIGN.md` as the style source.
- Run `npm run check` before review.
- Use `npm run dev -- --port 3017` for preview.
- Render only after script, storyboard, and content are approved.

## Cost-Control Rules

- Use one visual identity for all videos.
- Reuse the same title, outcomes, concept, example, checkpoint, and recap scene classes.
- Create diagrams in HTML/CSS where possible instead of commissioning custom animation.
- Use narration to carry detail; keep visuals clean.
- Batch-produce scripts before building videos.
- Build the first two module videos fully, then reuse the template.

## Quality Gates

- Learning outcomes are measurable.
- Quiz questions map to stated outcomes.
- Handout reinforces the video without duplicating every word.
- Lab activity is doable with free or low-cost simulation tooling.
- Video passes HyperFrames lint and layout inspection.
- No scene contains dense curriculum paragraphs.
