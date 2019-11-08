#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def movebase_client():

  client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
  client.wait_for_server()

  goal = MoveBaseGoal()

  goal.target_pose.header.frame_id = "base_link"
  goal.target_pose.header.stamp = rospy.Time.now()
  goal.target_pose.pose.position.x = 1.0;
  goal.target_pose.pose.orientation.w = 1.0;

  client.send_goal(goal)
  wait = client.wait_for_result()

  if not wait:
    rospy.logerr("Action server not available!")
    rospy.signal_shutdown("Action server not available!")
  else:
    return client.get_result()
