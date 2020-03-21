import rospy
import sys
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from tf.transformations import quaternion_from_euler
from geodesy.utm import fromLatLong
from geometry_msgs.msg import PoseStamped
import tf2_ros
import tf2_geometry_msgs

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

def init_gps_node(arguments):
    rospy.init_node('movebase_client_py')

    if len(arguments) < 3:
        rospy.logerr("Error: Insufficient Arguments - Usage is 'rosrun nav_goal movebase_client latitutde longitude'")
        rospy.signal_shutdown("Error: Insufficient Arguments - U Usage is 'rosrun nav_goal movebase_client latitutde longitude'")
        return 'Failure'
    else:
        try:
            lat = float(arguments[1])
            long = float(arguments[2])

            return (lat, long)
        except:
            rospy.logerr("Error: Incorrect Argument Types - All 2 arguments must be floats or integers.")
            rospy.signal_shutdown("Error: Incorrect Argument Types - All 2 arguments must be floats or integers.")
            return 'Failure'

def gps_to_map(lat, long):
    utm = fromLatLong(lat, long)

    # create PoseStamped message to set up for do_transform_pose 
    utm_pose = PoseStamped()
    utm_pose.header.frame_id = 'utm'
    utm_pose.pose.position.x = utm.easting
    utm_pose.pose.position.y = utm.northing

    # get the utm->odom transform using tf2_ros
    tfbuffer = tf2_ros.Buffer()
    tflistener = tf2_ros.TransformListener(tfbuffer)
    T = tfbuffer.lookup_transform('map', 'utm', rospy.Time(0), rospy.Duration(1.0))

    # apply the transform
    map_pose = tf2_geometry_msgs.do_transform_pose(utm_pose, T)
    
    return (map_pose.pose.position.x, map_pose.pose.position.y)

def map_to_utm(x, y):
    # create PoseStamped message to set up for do_transform_pose 
    map_pose = PoseStamped()
    map_pose.header.frame_id = 'map'
    map_pose.pose.position.x = x
    map_pose.pose.position.y = y

    # get the utm->odom transform using tf2_ros
    tfbuffer = tf2_ros.Buffer()
    tflistener = tf2_ros.TransformListener(tfbuffer)
    T = tfbuffer.lookup_transform('utm', 'map', rospy.Time(0), rospy.Duration(1.0))

    # apply the transform
    utm_pose = tf2_geometry_msgs.do_transform_pose(map_pose, T)
    
    return (utm_pose.pose.position.x, utm_pose.pose.position.y)

def movebase_client(x, y, yaw, frame):
    # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()

    # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()

    goal.target_pose.header.frame_id = frame
    goal.target_pose.header.stamp = rospy.Time.now()

    # Set goal position
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y

    # Convert yaw to quaternion and set pose
    q = quaternion_from_euler(0, 0, yaw)
    goal.target_pose.pose.orientation.x = q[0]
    goal.target_pose.pose.orientation.y = q[1]
    goal.target_pose.pose.orientation.z = q[2]
    goal.target_pose.pose.orientation.w = q[3]

    # Sends goal and waits until the action is completed (or aborted if it is impossible)
    client.send_goal(goal)

    rospy.loginfo("Goal of x:{} y:{} yaw:{} sent to action server!".format(x, y, yaw))

    wait = client.wait_for_result()

    # If the result doesn't arrive, assume the Server is not available
    if not wait:
        rospy.logerr("Error in retrieving action resolution! Exiting...")
        rospy.signal_shutdown("Error in retrieving action resolution! Exiting...")
    else:
        return client.get_goal_status_text()
