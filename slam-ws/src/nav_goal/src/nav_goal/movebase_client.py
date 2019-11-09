#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def movebase_client():
  # Create an action client called "move_base" with action definition file "MoveBaseAction"
  client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
  # Waits until the action server has started up and started listening for goals.
  client.wait_for_server()

  # Creates a new goal with the MoveBaseGoal constructor
  goal = MoveBaseGoal()

  goal.target_pose.header.frame_id = "base_link"
  goal.target_pose.header.stamp = rospy.Time.now()

  # Move 1.0 meters forward along the x axis of the "base_link" coordinate frame
  goal.target_pose.pose.position.x = 1.0;
  # No rotation of the mobile base frame w.r.t. base_link frame
  goal.target_pose.pose.orientation.w = 1.0;

  client.send_goal(goal)
  wait = client.wait_for_result()

  # If the result doesn't arrive, assume the Server is not available
  if not wait:
    rospy.logerr("Action server not available!")
    rospy.signal_shutdown("Action server not available!")
  else:
    return client.get_result()
