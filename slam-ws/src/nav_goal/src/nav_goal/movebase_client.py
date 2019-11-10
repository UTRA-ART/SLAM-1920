import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from tf.transformations import quaternion_from_euler

def movebase_client(x, y, yaw):
  # Create an action client called "move_base" with action definition file "MoveBaseAction"
  client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
  # Waits until the action server has started up and started listening for goals.
  client.wait_for_server()

  # Creates a new goal with the MoveBaseGoal constructor
  goal = MoveBaseGoal()

  goal.target_pose.header.frame_id = "base_link"
  goal.target_pose.header.stamp = rospy.Time.now()

  # Set goal position
  goal.target_pose.pose.position.x = x;
  goal.target_pose.pose.position.y = y;

  # Convert yaw to quaternion and set pose
  q = quaternion_from_euler(0, 0, yaw)
  goal.target_pose.pose.orientation.x = q[0];
  goal.target_pose.pose.orientation.y = q[1];
  goal.target_pose.pose.orientation.z = q[2];
  goal.target_pose.pose.orientation.w = q[3];

  # Sends goal and waits until the action is completed (or aborted if it is impossible)
  client.send_goal(goal)
  wait = client.wait_for_result()

  # If the result doesn't arrive, assume the Server is not available
  if not wait:
    rospy.logerr("Action server not available!")
    rospy.signal_shutdown("Action server not available!")
  else:
    return client.get_result()
