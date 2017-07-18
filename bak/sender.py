#!/usr/bin/env python2

import RFM69
from RFM69registers import *
import datetime
import time

NODE=1
NET=1
TIMEOUT=3
TOSLEEP=0.1

radio = RFM69.RFM69(RF69_433MHZ, NODE, NET, True)
print "Initializing......"

print "Reading all registers"
results = radio.readAllRegs()

print "Performing rcCalibration"
radio.rcCalibration()

print "setting high power"
radio.setHighPower(True)

print "Checking temperature"
print radio.readTemperature(0)

print "Initialization Complete!"
print "Start Sending..."

while True:

    msg = "I'm node %d" % (NODE)
    print "Sending " + msg
    if radio.sendWithRetry(1, msg, 3, 20):
        print "Ack recieved"

    if radio.ACKRequested():
        radio.sendACK()
    else:
        print "Ack not requested..."

print "shutting down"
radio.shutdown()



