// LeetCode 3829 - Design Ride Sharing System
// https://leetcode.com/problems/design_ride_sharing_system/

var RideSharingSystem = function() {
    this.t = 0;
    this.riders = new Map();
    this.drivers = new Map();
    this.d = new Map();
    this.riderKeys = [];
    this.driverKeys = [];
};

RideSharingSystem.prototype.addRider = function(riderId) {
    this.d.set(riderId, this.t);
    this.riders.set(this.t, riderId);
    this.riderKeys.push(this.t);
    this.t++;
};

RideSharingSystem.prototype.addDriver = function(driverId) {
    this.drivers.set(this.t, driverId);
    this.driverKeys.push(this.t);
    this.t++;
};

RideSharingSystem.prototype.matchDriverWithRider = function() {
    while (this.riderKeys.length && !this.riders.has(this.riderKeys[0])) this.riderKeys.shift();
    while (this.driverKeys.length && !this.drivers.has(this.driverKeys[0])) this.driverKeys.shift();
    if (!this.riderKeys.length || !this.driverKeys.length) return [-1, -1];
    const dKey = this.driverKeys.shift();
    const rKey = this.riderKeys.shift();
    const driverId = this.drivers.get(dKey), riderId = this.riders.get(rKey);
    this.drivers.delete(dKey);
    this.riders.delete(rKey);
    return [driverId, riderId];
};

RideSharingSystem.prototype.cancelRider = function(riderId) {
    if (!this.d.has(riderId)) return;
    this.riders.delete(this.d.get(riderId));
};
