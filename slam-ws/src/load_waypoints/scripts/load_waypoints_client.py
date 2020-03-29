#!/usr/bin/env python

import sys
import rospy, os, json 
from load_waypoints.srv import *

def load_waypoint_client(x):
    rospy.wait_for_service('load_waypoint')
    try:
        # Create handle for calling the service 
        load_waypoint = rospy.ServiceProxy('load_waypoint', LoadWaypoint)

        # This generates the LoadWaypointRequest object, and returns a LoadWaypointResponse object 
        resp = load_waypoint(x)
        return resp

    except rospy.ServiceException as e:
        print( "Service call failed: %s"%(e))

def usage():
    return "%s [x]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        x = int(sys.argv[1])
    else: # Incorrect user input 
        print (usage())
        sys.exit(1)
        
    print("Requesting waypoint #%s"%(x))
    print("Waypoint #%s is %s"%(x, load_waypoint_client(x)))
    