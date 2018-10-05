#!/usr/bin/env python

import roslib

import rospy
import tf
from nav_msgs.msg import Odometry

def handle_lidar_odom(msg, turtlename):
    br = tf.TransformBroadcaster()
    br.sendTransform((msg.x, msg.y, 0),
                     msg.quaternion,
                     rospy.Time.now(),
                     "base_footprint",,
                     "odom")

if __name__ == '__main__':
    rospy.init_node('laser_tf_broadcaster')
    turtlename = rospy.get_param('~turtle')
    rospy.Subscriber('/odom',
                    Odometry, handle_lidar_odom, turtlename)

    rospy.spin() 
