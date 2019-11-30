import rospy
import sys

def init_node(arguments):
    rospy.init_node('movebase_client_py')

    if len(arguments) < 4:
        rospy.logerr("Error: Insufficient Arguments - Usage is 'rosrun nav_goal movebase_client x y yaw' where x is distance to move in x, y is distance to move in y, and yaw is rotation in radians.")
        rospy.signal_shutdown("Error: Insufficient Arguments - Usage is 'rosrun nav_goal movebase_client x y yaw' where x is distance to move in x, y is distance to move in y, and yaw is rotation in radians.")
        return 'Failure'
    else:
        try:
            x = float(arguments[1])
            y = float(arguments[2])
            yaw = float(arguments[3])

            return (x, y, yaw)
        except:
            rospy.logerr("Error: Incorrect Argument Types - All 3 arguments must be floats or integers.")
            rospy.signal_shutdown("Error: Incorrect Argument Types - All 3 arguments must be floats or integers.")
            return 'Failure'
            