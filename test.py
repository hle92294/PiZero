from Beacon import Beacon
from random import randint
#import RFM69
from RFM69registers import *
import time
import json
import math
import numpy as np

TIMEOUT=3
TOSLEEP=0.1
#---------------------------#
#		SET COORDINATE		#
#---------------------------#
X1 = 9; Y1 = 2
X2 = 8; Y2 = 8
X3 = 2; Y3 = 8
b1 = Beacon(X1, Y1)
b2 = Beacon(X2, Y2)
b3 = Beacon(X3, Y3)
#---------------------------#
#		SUB-FUNCTION 		#
#---------------------------#

def _getMatrix_D():
	return np.array([[(2*(b2.x_coord - b1.x_coord)),(2*(b2.y_coord - b1.y_coord))], [(2*(b3.x_coord - b1.x_coord)), (2*(b3.y_coord - b1.y_coord))]])

def _getMatrix_Dx():
	return np.array([
		[((math.pow(b1.getDistance(), 2) - math.pow(b2.getDistance(), 2)) - (math.pow(b1.x_coord, 2) - math.pow(b2.x_coord, 2)) - (math.pow(b1.y_coord, 2) - math.pow(b2.y_coord, 2))), (2*(b2.y_coord - b1.y_coord))],
		[((math.pow(b1.getDistance(), 2) - math.pow(b3.getDistance(), 2)) - (math.pow(b1.x_coord, 2) - math.pow(b3.x_coord, 2)) - (math.pow(b1.y_coord, 2) - math.pow(b3.y_coord, 2))), (2*(b3.y_coord - b1.y_coord))]
		])

def _getMatrix_Dy():
	return np.array([
		[(2*(b2.x_coord - b1.x_coord)), ((math.pow(b1.getDistance(), 2) - math.pow(b2.getDistance(), 2)) - (math.pow(b1.x_coord, 2) - math.pow(b2.x_coord, 2)) - (math.pow(b1.y_coord, 2) - math.pow(b2.y_coord, 2)))],
		[(2*(b3.x_coord - b1.x_coord)), ((math.pow(b1.getDistance(), 2) - math.pow(b3.getDistance(), 2)) - (math.pow(b1.x_coord, 2) - math.pow(b3.x_coord, 2)) - (math.pow(b1.y_coord, 2) - math.pow(b3.y_coord, 2)))]
		])

def _converToFeet(distance_in_meter):
	return round((distance_in_meter * 3.280839895), 2)

def _switch(iD,rssi):
	if iD == 1: b1.setbeaconID(iD), b1.insertData(rssi)
	if iD == 2: b2.setbeaconID(iD), b2.insertData(rssi)
	if iD == 3: b3.setbeaconID(iD), b3.insertData(rssi)

#---------------------------#
#		MAIN-FUNCTION 		#
#---------------------------#

def main(): 
	
	print "Initializing......"
	sensor = RFM69.RFM69(RF69_433MHZ, 1, True)
	sensor.rcCalibration()
	sensor.setHighPower(True)
	D = _getMatrix_D()
	determinant_of_D = np.linalg.det(D)

	while True: 
		sensor.receiveBegin()
		timedOut=0
		while not sensor.receiveDone():
			timedOut+=TOSLEEP
			time.sleep(TOSLEEP)
			if timedOut > TIMEOUT:
				print "Waiting..."
				break
		iD = sensor.SENDERID
		rssi = sensor.RSSI
		if iD is not 0:_switch(iD,rssi)
		if b1.getRSSI()!=None and b2.getRSSI()!=None and b3.getRSSI()!=None:
			Dx = _getMatrix_Dx()
			X = round((np.linalg.det(Dx) / determinant_of_D),2)
			Dy = _getMatrix_Dy()
			Y = round((np.linalg.det(Dy) / determinant_of_D),2)
			print "({0}, {1})".format(X, Y) +  "in meter"
			print "({0}, {1})".format(_converToFeet(X), _converToFeet(Y)) + " in feet"
		else: print "No data receive!"

#main()
#---------------------------#
#		TEST SECTION 		#
#---------------------------#

counter = 1
D = _getMatrix_D()
determinant_of_D = np.linalg.det(D)
while (counter < 100):
	iD = randint(1,3)
	rssi = randint(50,65) * (-1)
	if iD != 0:_switch(iD,rssi)
	if b1.getRSSI()!=None and b2.getRSSI()!=None and b3.getRSSI()!=None:
		
		Dx = _getMatrix_Dx()
		X = round((np.linalg.det(Dx) / determinant_of_D),2)
		Dy = _getMatrix_Dy()
		Y = round((np.linalg.det(Dy) / determinant_of_D),2)
		print "({0}, {1})".format(X, Y) +  "in meter"
		print "({0}, {1})".format(_converToFeet(X), _converToFeet(Y)) + " in feet"
	else: print "No data receive!"
	counter = counter + 1
print b1.getData(), b1.getRSSI(), b1.getDistance(), _converToFeet(b1.getDistance())
print b2.getData(), b2.getRSSI(), b2.getDistance(), _converToFeet(b2.getDistance())
print b3.getData(), b3.getRSSI(), b3.getDistance(), _converToFeet(b3.getDistance())

