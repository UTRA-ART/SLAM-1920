#include "ros/ros.h"
#include "std_msgs/Float64.h"
#include "nav_msgs/Odometry.h"
#include "geometry_msgs/Twist.h"

double vx = 0.0;
double wz = 0.0;
double wheelbase = 0.91; // meters
double manual_control = 0.0;

void targetcb(const geometry_msgs::Twist& msg, bool active)
{
    if (active)
    {
        vx = msg.linear.x;
        wz = msg.angular.z;
    }
}

void targetcb_manual(const geometry_msgs::Twist& msg)
{
    targetcb(msg, manual_control == 1.0);
}

void targetcb_automatic(const geometry_msgs::Twist& msg)
{
    targetcb(msg, manual_control == 0.0);
}

void controlcb(const std_msgs::Float64& msg)
{
    manual_control = msg.data;
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "cmd_vel_to_motor");

    ros::NodeHandle n;
    ros::Time current_time, prev_time;

    current_time = ros::Time::now();

    // Subscribe to cmd_vel topics
    ros::Subscriber cmd_vel_manual_sub = n.subscribe("/cmd_vel2", 1, targetcb_manual);
    ros::Subscriber cmd_vel_automatic_sub = n.subscribe("/cmd_vel", 1, targetcb_automatic);
    ros::Subscriber stop_command_sub = n.subscribe("/stop_command", 1, controlcb);

    // Publish to right and left wheels
    ros::Publisher rvel_pub = n.advertise<std_msgs::Float64>("/right_wheel/command", 1);
    ros::Publisher lvel_pub = n.advertise<std_msgs::Float64>("/left_wheel/command", 1);

    ros::Rate loop_rate(100);

    std_msgs::Float64 rvelmsg;
    std_msgs::Float64 lvelmsg;	

    double v, vl, vr, rcommand, lcommand;

    while (n.ok())
    {
        // Check for msgs, updates xi, yi, zi, x, y, z
        ros::spinOnce();

        // NOTE: The following expressions are derived from unicycle kinematics
        vr = vx + (wheelbase * wz) / 2.0 ;
        vl = vx - (wheelbase * wz) / 2.0 ;

        rvelmsg.data = vr;
        lvelmsg.data = vl;

        rvel_pub.publish(rvelmsg);
        lvel_pub.publish(lvelmsg);

        loop_rate.sleep();
    }

    return 0;
}
