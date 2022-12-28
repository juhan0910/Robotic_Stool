#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
#from std_msgs.msg import String
from std_msgs.msg import Int64

class turtle1:
    def __init__(self):
        rospy.Subscriber("chatter", Int64, self.callback)

    def callback(self, data):
        rospy.loginfo("I'm moving to %s", data.data)

        if data.data == 1:
           result = self.movebase_client(-1.3,1.5,0)
           if result:
               rospy.loginfo("position 1 arrived!")
          
   	elif data.data == 2:
           result = self.movebase_client(-0.8,1.5,0)
           if result:
               rospy.loginfo("position 2 arrived!")

        elif data.data == 3:
           result = self.movebase_client(-0.3,1.5,0)
           if result:
               rospy.loginfo("position 3 arrived!")

        elif data.data == 4:
           result = self.movebase_client(0.3,2.0,0)
           if result:
               rospy.loginfo("position 4 arrived!")


    def movebase_client(self,x,y,z):

	client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
	client.wait_for_server()

	goal = MoveBaseGoal()
	goal.target_pose.header.frame_id = "map"
	goal.target_pose.header.stamp = rospy.Time.now()
	goal.target_pose.pose.position.x = x
 	goal.target_pose.pose.position.y = y
    	goal.target_pose.pose.orientation.z = z
    	goal.target_pose.pose.orientation.w = 1.0

    	client.send_goal(goal)
	
	#return 1
    	wait = client.wait_for_result()
        if not wait:
        	rospy.logerr("Action server not available!")
        	rospy.signal_shutdown("Action server not available!")
        else:
        	return client.get_result()

if __name__ == '__main__':

    rospy.init_node('turtle1', anonymous=False)
    turtle1()
    rospy.spin()
