import math
import numpy as np
TX_POWER = -40
SIG_PROP = 2.0

class Beacon(object):
    """A vehicle for sale by Jeffco Car Dealership.

  Attributes:
      beaconID:
      RSSI: The rssi value from rf433
      x_coord: Given X axis of the beacon location
      y_coord: Given y axis of the beacon location
      distance: distance calculated using propergration formular from the receiver to the beacon
      android_distance: distance calculated using android formular from the receiver to the beacon
  """
    def __init__(self, x_coord=0, y_coord=0):
        self.beaconID = None
        self.rssi = None
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.data = []

    def setbeaconID(self, beaconID):
        self.beaconID = beaconID

    def setRSSI(self, rssi):
        self.clearData()
        self.rssi = rssi

    def getbeaconID(self):
        if self.beaconID is not None:
          return self.beaconID

    def getRSSI(self):
        if self.rssi is not None:
          return self.rssi

    def getCoordinate(self):
        if self.rssi is not None:
          return "({0}, {1})".format(self.x_coord, self.y_coord)
        return "ERROR: No RSSI value!"
    
    def getDistance(self):
        if self.rssi is not None:
          return (round(math.pow(10, (TX_POWER - self.rssi) / (10 * SIG_PROP)), 3))
        return "ERROR: No RSSI value!"
    
    def getAndroid_distance(self):
        if self.rssi is not None:
          return (round(((0.89976) * math.pow((self.rssi / TX_POWER), 7.7095) + 0.111) ,3))
        return "ERROR: No RSSI value!"

    def getData(self):
        if len(self.data) is 0: return "ERROR: No Data!"
        return self.data

    def insertData(self, rssi):
        if len(self.data) > 10: self.data.pop(0)
        self.data.append(rssi)
        self.rssi = reduce(lambda x, y: x + y, self.data) / len(self.data)

    def clearData(self):
        if len(self.data) != 0: self.data = []








