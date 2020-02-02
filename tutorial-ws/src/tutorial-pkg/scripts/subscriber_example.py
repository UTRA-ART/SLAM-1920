#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback_fnc(data):
  rospy.loginfo(rospy.get_caller_id() + " " + "I heard %s", data.data)

def subscriber_example():
    rospy.init_node('subscriber_example')
    sub = rospy.Subscriber('chatter', String, callback_fnc)
    
    rospy.spin() #listen for data.

if __name__ == '__main__':
    try:
        subscriber_example()
    except rospy.ROSInterruptException:
        pass
