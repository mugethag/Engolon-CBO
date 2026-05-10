# Simulation Lab 01

Lab title: Mobile Robot and Drone Control Foundations

Connected modules:

- Module 1: Introduction to Sustainability Robotics and Intelligent Systems
- Module 2: Introduction to Drone Systems, Aerial Robotics and Control Design Fundamentals

Estimated learner time: 2-3 hours

## Lab Purpose

This lab helps learners connect robotic subsystems, feedback control, motion behavior, and drone control concepts using simulation.

The lab can be completed with a free or low-cost simulation environment. Recommended options include Webots, CoppeliaSim Edu, Gazebo, MATLAB/Simulink if institutionally available, or a simple browser-based control simulator created later for the course.

## Learning Outcomes

By the end of this lab, learners should be able to:

1. Identify sensors, actuators, controller, and feedback in a simulated robot.
2. Observe how command changes affect robot motion.
3. Compare open-loop and closed-loop behavior.
4. Describe overshoot, oscillation, settling, and error.
5. Connect drone altitude control to general feedback control ideas.
6. Reflect on how simulation reduces cost and risk before real-world deployment.

## Required Simulation Scenario

Learners complete two short simulation tasks:

1. Ground robot target approach
2. Drone altitude hold concept

If a drone simulator is not available, the altitude hold task may be completed using a one-dimensional vertical motion model or an instructor-provided graphing activity.

## Part A: Ground Robot Target Approach

### Scenario

A mobile robot must move from a starting point to a target position. The learner compares behavior with and without feedback correction.

### Steps

1. Open the selected simulator.
2. Load or create a simple mobile robot scene.
3. Set a target position one to three meters away from the start.
4. Run an open-loop attempt where the robot drives forward for a fixed time.
5. Record whether the robot reaches, undershoots, overshoots, or drifts away from the target.
6. Run a feedback-based attempt where sensor or position feedback is used to reduce target error.
7. Record the final error and describe the motion behavior.

### Evidence To Submit

- Screenshot of the simulation setup.
- Screenshot or note showing the final robot position.
- Short table comparing open-loop and closed-loop behavior.

## Part B: Drone Altitude Hold Concept

### Scenario

A drone or vertical-motion model must reach and hold a target altitude.

### Steps

1. Set a target altitude.
2. Run a low-response control setting.
3. Observe whether the system responds slowly or fails to reach target altitude.
4. Run a high-response control setting.
5. Observe whether the system overshoots or oscillates.
6. Run a balanced response setting if available.
7. Describe which behavior seems most stable and why.

### Evidence To Submit

- Screenshot of altitude behavior or a hand-drawn response graph.
- Notes describing overshoot, oscillation, settling, and steady-state error.
- One paragraph explaining how feedback control is being used.

## Lab Worksheet

| Prompt | Learner Response |
| --- | --- |
| Which sensors or measurements did the robot use? |  |
| Which actuators produced movement? |  |
| What command was given? |  |
| What was the actual response? |  |
| What error did you observe? |  |
| How did feedback change the behavior? |  |
| Did the system overshoot or oscillate? |  |
| What setting or design choice improved stability? |  |

## Reflection

Write 250-400 words responding to the following:

How did simulation help you understand robotic and drone control before working with physical hardware? In your answer, refer to sensors, actuators, feedback, stability, and one sustainability or safety benefit of simulation.

## Assessment Rubric

| Criteria | Excellent | Satisfactory | Needs Improvement |
| --- | --- | --- | --- |
| Subsystem identification | Correctly identifies sensors, actuators, controller, and feedback | Identifies most subsystems | Missing or confused subsystem descriptions |
| Control behavior analysis | Clearly explains command, response, error, overshoot, oscillation, and stability | Explains basic behavior with minor gaps | Little evidence of control reasoning |
| Evidence submission | Provides clear screenshots or graphs and comparison table | Provides partial evidence | Evidence missing or unclear |
| Reflection quality | Connects simulation to safety, sustainability, and learning | Gives a basic reflection | Reflection is too brief or unrelated |

## Instructor Notes

- This MVP lab is intentionally simulator-neutral.
- If the institution selects a standard platform, replace the generic steps with exact installation and scene instructions.
- A later course version can include downloadable starter simulation files.
- Keep the first lab focused on observation and reasoning, not advanced coding.
