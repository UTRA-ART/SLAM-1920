cmake_minimum_required(VERSION 2.8.3)
project(nav_goal)

find_package(catkin REQUIRED COMPONENTS
  actionlib
  move_base_msgs
  rospy
)

catkin_python_setup()
catkin_install_python(PROGRAMS bin/movebase_client DESTINATION ${PROJECT_NAME}/bin)

#catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES nav_goal
#  CATKIN_DEPENDS actionlib move_base_msgs rospy
#  DEPENDS system_lib
#)
