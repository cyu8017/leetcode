# LeetCode 3829 - Design Ride Sharing System
# https://leetcode.com/problems/design-ride-sharing-system/

from typing import List


class RideSharingSystem:
    def __init__(self):
        self.t = 0
        self.riders = {}
        self.drivers = {}
        self.d = {}
        self.riderKeys = []
        self.driverKeys = []

    def addRider(self, riderId: int) -> None:
        self.d[riderId] = self.t
        self.riders[self.t] = riderId
        self.riderKeys.append(self.t)
        self.t += 1

    def addDriver(self, driverId: int) -> None:
        self.drivers[self.t] = driverId
        self.driverKeys.append(self.t)
        self.t += 1

    def matchDriverWithRider(self) -> List[int]:
        while self.riderKeys and self.riderKeys[0] not in self.riders:
            self.riderKeys.pop(0)
        while self.driverKeys and self.driverKeys[0] not in self.drivers:
            self.driverKeys.pop(0)
        if not self.riderKeys or not self.driverKeys:
            return [-1, -1]
        dKey = self.driverKeys.pop(0)
        rKey = self.riderKeys.pop(0)
        driverId = self.drivers.pop(dKey)
        riderId = self.riders.pop(rKey)
        return [driverId, riderId]

    def cancelRider(self, riderId: int) -> None:
        if riderId not in self.d:
            return
        self.riders.pop(self.d[riderId], None)
