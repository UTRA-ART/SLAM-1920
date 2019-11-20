cmake_minimum_required(VERSION 2.8.3)
project(nav_amcl)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  move_base
  nav_msgs
  rospy
  sensor_msgs
  std_msgs
  tf
)
