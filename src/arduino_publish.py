#!/usr/bin/env python
import rospy
import serial
from std_msgs.msg import Int32

rospy.init_node('serial_monitor')

port='/dev/ttyUSB0'
baud=115200
data=rospy.Publisher('arduino_data',Int32,queue_size=10)
rate=rospy.Rate(10)
ser=serial.Serial(port,baud)
temp=(ser.readline())
a=ser.readline().rstrip()
b=ser.readline().rstrip()
c=ser.readline().rstrip()
d=ser.readline().rstrip()

while not rospy.is_shutdown():
	data.publish(int(a))
	data.publish(int(b))
	data.publish(int(c))
	data.publish(int(d))
	rate.sleep()
