#!/usr/bin/env python

import rospy, os, json 
from load_waypoints.srv import *

all_waypoints = list()

def populate_waypoint_table():
    base_dir = rospy.get_param('~arg_name') # ~ added to arg_name because private param 
    
    with open(base_dir + '/scripts/waypoints.json') as f:
        data = json.load(f)

    # Parse through dictionary and create list of lists holding all waypoints
    for waypoint in data["waypoints"]:
        all_waypoints.append([waypoint['coordinate 1'], waypoint['coordinate 2']])

    print("Loaded waypoints:", all_waypoints)
    return 

def handle_waypoint_number(req):
    print ("Returning request for waypoint #%s "%(req.waypoint_number))
    return LoadWaypointResponse(all_waypoints[req.waypoint_number])

def load_waypoints_server():
    # Must init node before reading any files
    rospy.init_node('load_waypoints_server')
    parse_json()
    s = rospy.Service('load_waypoint', LoadWaypoint, handle_waypoint_number)
    print("Ready to load waypoints.")
    rospy.spin() # Keeps code from exiting until the service is shutdown

if __name__ == "__main__":
    load_waypoints_server()
    
