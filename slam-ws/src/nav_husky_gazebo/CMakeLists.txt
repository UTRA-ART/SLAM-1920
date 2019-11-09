cmake_minimum_required(VERSION 2.8.3)
project(nav_husky_gazebo)

find_package(catkin REQUIRED COMPONENTS
  move_base
  nav_msgs
  rospy
  sensor_msgs
  std_msgs
  tf
)
