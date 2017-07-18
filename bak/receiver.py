#!/usr/bin/env python2

import RFM69
from RFM69registers import *
import datetime
import time

NET=1
TIMEOUT=3
TOSLEEP=0.1

radio = RFM69.RFM69(RF69_433MHZ, NET, True)
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
print "Start Receiving..."

while True:

    radio.receiveBegin()
    timedOut=0
    while not radio.receiveDone():
        timedOut+=TOSLEEP
        time.sleep(TOSLEEP)
        if timedOut > TIMEOUT:
            print "Waiting..."
            break
    print "Data: %s Node: %s RSSI:%s" % ("".join([chr(letter) for letter in radio.DATA]), radio.SENDERID, radio.RSSI)

    if radio.ACKRequested():
        print "Sending ack..."
        radio.sendACK()
    else:
        print "Ack not requested..."

print "shutting down"
radio.shutdown()


