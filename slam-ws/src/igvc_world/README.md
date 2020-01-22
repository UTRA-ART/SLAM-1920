# usma_gazebo
Instructions on how to set up Gazebo for USMA Projects.

## IGVC Basic Course Gazebo Simulation
Forked from this repo: https://github.com/MST-Robotics/IGVC

1. Install Gazebo ROS packages following this [tutorial] (http://gazebosim.org/tutorials?tut=ros_installing). Currently, we are use ROS Indigo.
2. Clone the usma_gazebo ros package into your catkin workspace src folder.
 - `cd ~/catkin_ws/src`
 - `git clone https://github.com/westpoint-robotics/usma_gazebo.git usma_gazebo`
3. Install the models into the gazebo models folder.
 - `cd ~/catkin_ws/src/usma_gazebo/models`
 - `./install_models.sh`
4. Build src
 - `cd ~/catkin_ws/`
 - `catkin_make`
5. Launch igvc_basic_course
 - `roslaunch usma_gazebo igvc_basic_course.launch`
