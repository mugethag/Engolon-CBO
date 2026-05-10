# Learner Handout: Module 2

Module: Introduction to Drone Systems, Aerial Robotics and Control Design Fundamentals

## Big Idea

A drone is an aerial robotic system. Stable and useful drone behavior depends on propulsion, power, sensors, flight control, communication, payload design, feedback, and mission-specific autonomy.

## Core Drone Subsystems

| Subsystem | Function |
| --- | --- |
| Frame | Physical structure that holds components |
| Propulsion | Motors and propellers that generate lift and movement |
| Power | Battery and power distribution |
| Sensors | Estimate altitude, orientation, position, speed, and environment |
| Flight controller | Processes sensor data and commands motors |
| Communication link | Connects drone to operator, base station, or network |
| Payload | Mission equipment such as camera, sensor, package, or inspection tool |

## Flight Axes

| Axis | Meaning |
| --- | --- |
| Roll | Tilting left or right |
| Pitch | Tilting forward or backward |
| Yaw | Rotating around the vertical axis |
| Altitude | Height above a reference point |

## Control Design Language

- Command: what the system is asked to do.
- Response: how the system actually behaves.
- Error: the difference between desired and actual behavior.
- Stability: whether the system settles into acceptable behavior.
- Overshoot: when the system goes beyond the target.
- Oscillation: repeated movement above and below a target.
- Disturbance: an external effect such as wind or sensor noise.

## PID Controller Memory Aid

- P: present error
- I: accumulated error
- D: rate of change of error

## Basic Autonomy Stack

1. Perception: detect relevant environment information.
2. Localization: estimate where the drone is.
3. Planning: choose a path or action.
4. Control: convert the plan into motion commands.
5. Mission monitoring: check safety, progress, and constraints.

## Reflection Prompt

Choose one drone mission: environmental monitoring, bridge inspection, disaster response, agriculture, or mapping. List the payload, sensors, control priorities, and safety concerns for that mission.
