import rospy
from mavros_msgs.msg import State
from mavros_msgs.srv import CommandBool, SetMode
from geometry_msgs.msg import Pose, PoseStamped, Point, Quaternion
import math
import numpy as np
from geometry_msgs.msg import Twist, TwistStamped
from nav_msgs.msg import Odometry
from std_msgs.msg import Header, String , Int8
from threading import Thread
import serial

global take_off
take_off=1

def start():
	result = arming_srv(value=True)
	print result
	result = mode_srv(custom_mode="OFFBOARD")
	print result
	
	while not rospy.is_shutdown():
	        pos=set_position()
	        print "Setting Offboard Mode"
	        result = mode_srv(custom_mode="OFFBOARD")
	        print result
	        pos.header.stamp = rospy.Time.now()
	        print pos
	        vel_pub.publish(pos)
	        print "ok"
	        try:
	           rate.sleep()
	           print "sleep"
	        except rospy.ROSInterruptException:
	           pass
          
def set_position():
	port='/dev/ttyACM0'
	baud=9600
	ser=serial.Serial(port,baud)
	if (ser.readline()=='@\r\n'):
		a=ser.readline().rstrip()
		b=ser.readline().rstrip()
		c=ser.readline().rstrip()
		d=ser.readline().rstrip()
		e=ser.readline().rstrip()
	
	global hold
	global holdkm1
	global hold_refr
	hold=0
	pos=TwistStamped()
	pos.twist=Twist()
	pos.header = Header()
	if int(a)>1000:
		pos.twist.linear.z=1
		print a 
	elif int(b)>1000:
		pos.twist.linear.x=0.8
		print b
	elif int(c)>1000:
		pos.twist.linear.x=-0.8
		print c
	elif int(d)>1000:
		pos.twist.linear.y=0.8
		print d
	elif int(e)>1000:
		pos.twist.linear.y=-.8
		print e	
	return pos

if __name__ == '__main__':
    rospy.init_node('mind_control', anonymous=True)
    rate=rospy.Rate(10)
    vel_pub = rospy.Publisher('/mavros/setpoint_velocity/cmd_vel', TwistStamped,queue_size=10)
    arming_srv = rospy.ServiceProxy("/mavros/cmd/arming", CommandBool)
    mode_srv = rospy.ServiceProxy("/mavros/set_mode", SetMode)
    start()
