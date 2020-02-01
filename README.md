# SLAM on ROS #

This project runs on ROS Kinetic for Ubuntu 16.04

## Setting up the ROS Environment ##
1. Perform ROS Kinetic full install. See [Getting Started with ROS](https://github.com/UTRA-ART/SLAM/wiki#getting-started-with-ros) for installation instructions.
2. Install husky desktop and simulator. See: [Clearpath ROS Tutorial](https://www.clearpathrobotics.com/assets/guides/ros/Drive%20a%20Husky.html) or [Husky Simulation Wiki](http://wiki.ros.org/husky_gazebo/Tutorials/Simulating%20Husky) for details.
Run:
```
$ sudo apt-get update
$ sudo apt-get install ros-kinetic-husky-desktop
$ sudo apt-get install ros-kinetic-husky-simulator
```
3. Install the Navigation Stack: `sudo apt-get install ros-kinetic-navigation`
4. Install gmapping (SLAM package): `sudo apt-get install ros-kinetic-gmapping`

## Creating the ROS Workspace ##
First clone the git repository, then create a workspace. After run:
```
# Creates CMake file in src
$ mkdir -p ./slam-ws/src  # These folders already exist on Github, so don't run this line
$ cd ./slam-ws/src
$ catkin_init_workspace

# Creates setup files - build/ and devel/ folders
$ cd ./slam-ws
$ catkin_make
```

## Cleaning ##
Every once in a while it is necessary to clear unnecesary logs that are saved from tests that have been run. These logs can quickly add up to the GB range, and can slow down ROS. To check how many logs you have run:

```
$ rosclean check
```

This should give you how much memory is consumed by logs. If nothing is returned you have no logs. 
To delete logs run:

```
$ rosclean purge
``` 

## Setting up ROS Serial for motor node ##
ROS Serial is used to communicate with Arduinos to control the motors and read from the wheel encoders. The general set up is as follows:
```
ROS (cmd_vel/odom) <--> via rosserial (USB) <--> Arduino UNO (motors/wheel encoders)
```
In order to communicate between ROS and Arduino via a serial connection (which is how we communicate with the Motors and Wheel Encoders), we must install the [`rosserial_arduino`](http://wiki.ros.org/rosserial_arduino) package:
```
$ sudo apt-get install ros-kinetic-rosserial-arduino
```

Before launching the `motor_control` ROS node, ensure that:
- the Arduino has been flashed with the appropriate code (See **Side Note**)
- the Arduino is connected to `/dev/ttyACM[X]`
- `/dev/ttyACM[X]` has read and write permissions (`chmod a+rw /dev/ttyACM[X]`)

To enable control of the motors via `cmd_vel` run:
```
# Re-routes cmd_vel to cmd_vel_to_motor node to communicate with Arduino motors
# NOTE: Also enables communication with the Arduino wheel encoders

$ roslaunch motor_control motor_control.launch
```

### Side Note: ###
To Flash the Arduino with the Motor or Encoder code:
- Install the Arduino IDE
- Add the ROS libraries to by navigating to `<sketchbook>/libraries`(where `<sketchbook>` is usually `Sketchbook` or `Arduino`) and running `rosrun rosserial_arduino make_libraries.py .`
- Compile the file you want using the Arduino IDE (either `motorcontrol.ino` or `encoders.ino`)
- Upload the compiled code to the Arduino connected to the USB port (give permissions to the correct USB port)

**NOTE:** When connecting the motors and wheel encoders, first plug in the motor Arduino (so it can be recognized as `ttyACM0`) and then the encoders Arduino.

## Useful ROS Resources ##
- [ROS Wiki](http://wiki.ros.org)
- [A Gentle Introduction to ROS](https://cse.sc.edu/~jokane/agitr/agitr-letter.pdf)
- [Programming with ROS](http://marte.aslab.upm.es/redmine/files/dmsf/p_drone-testbed/170324115730_268_Quigley_-_Programming_Robots_with_ROS.pdf?fbclid=IwAR2iVBeZ9WQu1uG614YMamUZlxvd8nJoHbxW5BntgaEjgVI4MBOzqOCdYi8)
