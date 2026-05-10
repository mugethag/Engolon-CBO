# Scene-by-Scene Storyboard

## Video 1: Program Orientation

Format: 1920 x 1080, 16:9, fully online CBI orientation.

Visual identity: dark editorial Engolon style with technical robotics overlays. See `DESIGN.md`.

## Production Storyboard

| Scene | Time | Narration Purpose | Visual Direction | Reusable Template Role |
| --- | ---: | --- | --- | --- |
| 1. Opening title | 0:00-0:30 | Welcome learners and name the certificate. | Engolon logo, certificate title, EQF Level 6, 60 ECTS, online mode. Subtle robotics grid and sensor nodes. | Title opener for every module. |
| 2. Program architecture | 0:30-1:00 | Explain duration, credits, and online format. | Three credential tiles and a two-year pathway line. | Credential/overview scene. |
| 3. Learning outcomes | 1:00-1:45 | Present major graduate capabilities. | Seven outcome cards grouped around robotics, AI, swarm systems, cybersecurity, ethics, quantum concepts, and sustainability. | Outcomes scene for each module. |
| 4. Year 1 pathway | 1:45-2:25 | Show foundational progression. | Three term columns: core robotics/drones/control, autonomy/swarms/environmental monitoring, AI/cybersecurity/decision-making. | Timeline scene. |
| 5. Year 2 pathway | 2:25-3:05 | Show advanced progression. | Three term columns: infrastructure/construction robotics, perception/AI/quantum systems, capstone. | Timeline continuation scene. |
| 6. Capstone integration | 3:05-3:45 | Explain the final applied project. | Central autonomous system diagram linking perception, control, AI, cybersecurity, sustainability, and evaluation. | Capstone/project brief scene. |
| 7. Closing | 3:45-4:15 | Reinforce professional and responsible design. | Final statement, learner-ready outcomes, Engolon mark. | Closing scene. |

## HyperFrames Production Mapping

The implemented `index.html` now follows the full 4:15 production storyboard:

| Production Scene | Time | Full Storyboard Equivalent |
| --- | ---: | --- |
| `scene-title` | 0:00-0:30 | Scene 1 |
| `scene-architecture` | 0:30-1:00 | Scene 2 |
| `scene-outcomes` | 1:00-1:45 | Scene 3 |
| `scene-year-one` | 1:45-2:25 | Scene 4 |
| `scene-year-two` | 2:25-3:05 | Scene 5 |
| `scene-capstone` | 3:05-3:45 | Scene 6 |
| `scene-close` | 3:45-4:15 | Scene 7 |

## Student-Ready Use

- Use `index.html` as the source composition for the full course orientation video.
- Render the composition to MP4 before publishing to the Engolon website or LMS.
- Keep this orientation as the first item students complete before Term 1 Module 1.
- Pair the video with `course-mvp/README.md` and `course-mvp/term-1/course-map.md` inside the LMS.

## On-Screen Text Principles

- Keep each scene to one core instructional idea.
- Use short labels instead of full curriculum sentences.
- Put narration detail in audio or captions, not in dense slide text.
- Preserve the term/module structure so learners understand the certificate pathway.
- Use the same scene classes for future module videos so colors, timing, and layout stay consistent.
