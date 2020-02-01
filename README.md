# SLAM on ROS #

This project runs on ROS Kinetic for Ubuntu 16.04. Please check out our [Wiki](https://github.com/UTRA-ART/SLAM/wiki#getting-started-with-ros) for more information.

## Setting up the ROS Environment ##

### Install ROS Kinetic
See [Getting Started with ROS](https://github.com/UTRA-ART/SLAM/wiki#getting-started-with-ros) for installation instructions.

### Install the [husky-desktop]() and [husky-simulator]() Packages
```$ sudo apt-get update
$ sudo apt-get install ros-kinetic-husky-desktop
$ sudo apt-get install ros-kinetic-husky-simulator
```

### Install the [navigation](http://wiki.ros.org/navigation) Package
```
sudo apt-get install ros-kinetic-navigation
```

### Install the [gmapping](http://wiki.ros.org/gmapping) Package:
```
sudo apt-get install ros-kinetic-gmapping
```
> **Note:** This is the package we use for performing SLAM.

## Creating the ROS Workspace
First clone the git repository, then create a workspace by running
```
# Creates CMake file in src
$ mkdir -p ./slam-ws/src  # These folders already exist on Github, so don't run this line
$ cd ./slam-ws/src
$ catkin_init_workspace

# Creates setup files - build/ and devel/ folders
$ cd ./slam-ws
$ catkin_make
```

### Cleaning the ROS Workspace 
Every once in a while it is necessary to clear unnecesary logs that are saved from tests that have been run. These logs can quickly add up to the GB range, and can slow down ROS. To check how many logs you have run:

```
$ rosclean check
```

This should give you how much memory is consumed by logs. If nothing is returned you have no logs. 
To delete logs run:

```
$ rosclean purge
``` 
