#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def publisher_example():
    rospy.init_node('publisher_example')
    pub = rospy.Publisher('chatter', String, queue_size = 10)
    rate = rospy.Rate(10) #10 Hz.

    while not rospy.is_shutdown():
        message = "Hello %s" % rospy.get_time()
        pub.publish(message)
        rospy.loginfo(rospy.get_caller_id() + " " + "I said %s" % message)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher_example()
    except rospy.ROSInterruptException:
        pass
