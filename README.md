# SLAM on ROS #

This project runs on ROS Kinetic for Ubuntu 16.04

## Setting up the ROS Environment ##
1. Perform ROS Kinetic full install. See: [ROS Kinetic Installation](http://wiki.ros.org/kinetic/Installation/Ubuntu)
2. Install husky desktop and simulator. See: [Clearpath ROS Tutorial](https://www.clearpathrobotics.com/assets/guides/ros/Drive%20a%20Husky.html) or [Husky Simulation Wiki](http://wiki.ros.org/husky_gazebo/Tutorials/Simulating%20Husky).
Run:
```
$ sudo apt-get update
$ sudo apt-get install ros-kinetic-husky-desktop
$ sudo apt-get install ros-kinetic-husky-simulator
```
3. Install the Navigation Stack: `sudo apt-get install ros-kinetic-navigation`

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

## Creating a Package for using the Navigation Stack ##
**NOTE:** Do not execute this section, it's just documentation to how the nav_husky_gazebo package was set up.
1. Create the nav_husky_gazebo package with its dependencies:
```
$ catkin_create_pkg nav_husky_gazebo rospy move_base nav_msgs sensor_msgs std_msgs tf
```
2. Create 4 .yaml configuration files in `config/`:
    - costmap common
    - local costmap
    - global costmap
    - local base planner
- **NOTE:** Consult [ROS nav stack SetUp](http://wiki.ros.org/navigation/Tutorials/RobotSetup) and the [Husky Github](https://github.com/husky/husky) to see how the parameters were selected. Specifically look at the Husky URDF on the Github.
3. Create launch file for Navigation Stack `launch/move_base.launch`.
4. Run `$ catkin_make` to and then `source slam-ws/devel/setup.bash`. This will build the package (needs to be done everytime it is edited?)
    - **NOTE:** I forgot what it exactly does but it's something along the lines of making the package available to ROS. These two commands must be run anytime a new package is added.

To run the Navigation Stack:
```
# Start up the Robot in simulation
$ roslaunch husky_gazebo husky_empty_world.launch

# Start up the Navigation Stack
$ roslaunch .../launch/move_base.launch
```

### Useful ROS Resources ###
- [ROS Wiki](http://wiki.ros.org)
- [A Gentle Introduction to ROS](https://cse.sc.edu/~jokane/agitr/agitr-letter.pdf)
- [Programming with ROS](http://marte.aslab.upm.es/redmine/files/dmsf/p_drone-testbed/170324115730_268_Quigley_-_Programming_Robots_with_ROS.pdf?fbclid=IwAR2iVBeZ9WQu1uG614YMamUZlxvd8nJoHbxW5BntgaEjgVI4MBOzqOCdYi8)
