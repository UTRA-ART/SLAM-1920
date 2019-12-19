# SLAM on ROS #

This project runs on ROS Kinetic for Ubuntu 16.04

## Setting up the ROS Environment ##
1. Perform ROS Kinetic full install. See: [ROS Kinetic Installation](http://wiki.ros.org/kinetic/Installation/Ubuntu)
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
ROS Serial is used to communicate with the Arduino to control the motors.

cmdvel -->  rosserial_python --> Arduino UNO

1. Add the sensors package(https://github.com/UTRA-ART/UTRA_ART/tree/master/UTRA_ws/src/sensors) into your workspace and run catkin_make on it
2. source the devel/setup.bash of the sensors node.
3. Launch arduino.launch from sensors/src/rosserial_python/launch/arduino.launch using roslaunch
4. It should run three ros nodes, 2 encoders and 1 motor node. The encoders are *not* necessary for running the motor
5. Make sure the Arduino is connected to /dev/ttyACM0 to interface with it. Also give write and executable permissions to it (`sudo chmod a+x /dev/ttyACM0`)



### Useful ROS Resources ###
- [ROS Wiki](http://wiki.ros.org)
- [A Gentle Introduction to ROS](https://cse.sc.edu/~jokane/agitr/agitr-letter.pdf)
- [Programming with ROS](http://marte.aslab.upm.es/redmine/files/dmsf/p_drone-testbed/170324115730_268_Quigley_-_Programming_Robots_with_ROS.pdf?fbclid=IwAR2iVBeZ9WQu1uG614YMamUZlxvd8nJoHbxW5BntgaEjgVI4MBOzqOCdYi8)
