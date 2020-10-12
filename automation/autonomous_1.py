import time
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from pymavlink import mavutil
import Tkinter as tk
import os
from time import sleep
import serial

vehicle = connect("/dev/ttyUSB0", baud = 57600)
time.sleep(6)
print("CONNECTED")
print("the drone is now connected")
print("Kindly stand away from the drone")
vehicle.mode = VehicleMode("GUIDED")
print("MODE SET TO GUIDED")
reached = False
time.sleep(2)
def arm():
	print("Arming motors")
	while vehicle.armed!=True:
		vehicle.armed = True
		time.sleep(6)

def arm_and_takeoff(altitude):
	arm()
	print("Taking Off")
	vehicle.simple_takeoff(altitude)
	time.sleep(2)
	while True:
		v_alt = vehicle.location.global_relative_frame.alt
		print("Altitude = %f m"%v_alt)
		if v_alt >= altitude - 0.1:
			print("Target altitude reached")
			break
		time.sleep(1)
	global reached
	reached = True
	print("reached target")
	
while True:
	vehicle.mode = VehicleMode("GUIDED")
	time.sleep(2)
	arm_and_takeoff(4)
	print("takeoff")
	time.sleep(10)		
	print("Mode Set to LAND")
	
	vehicle.mode = VehicleMode("LAND")
	while vehicle.armed == True:
		print("Setting Reached to False")
		time.sleep(1)
		reached = False

