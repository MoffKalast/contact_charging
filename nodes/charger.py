#!/usr/bin/env python

from __future__ import print_function

import rospy
import actionlib
import math
import traceback
import tf2_ros
import time
from actionlib_msgs.msg import *

#import docking.srv as docking
from geometry_msgs.msg import PoseStamped, TransformStamped, Twist, Vector3Stamped
from fiducial_msgs.msg import FiducialTransformArray, FiducialTransform
from actionlib_msgs.msg import GoalStatusArray, GoalStatus
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from tf2_geometry_msgs import do_transform_vector3
from tf.transformations import quaternion_from_euler, euler_from_quaternion

# Utility function to convert radians to degrees
def degrees(r):
    return 180.0 * r / math.pi

def radians(d):
    return d * math.pi / 180.0

class Charger:

	def __init__(self):
		rospy.init_node("contact_charger")
		self.buffer = tf2_ros.Buffer()
		self.listener = tf2_ros.TransformListener(self.buffer)
		self.broadcaster = tf2_ros.TransformBroadcaster()
		self.client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
		self.client.wait_for_server()
		self.fid_subscriber = rospy.Subscriber("/fiducial_transforms", FiducialTransformArray, self.fiducial_callback)

	def fiducial_callback(data):
		self.fidcall = rospy.loginfo(data)

try:
	x = Charger()
	print(x().fidcall)
	rospy.spin()
except rospy.ROSInterruptException:
	print("Script interrupted", file=sys.stderr)