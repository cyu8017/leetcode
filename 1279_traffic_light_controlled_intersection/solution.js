// LeetCode 1279 - Traffic Light Controlled Intersection
// https://leetcode.com/problems/traffic-light-controlled-intersection/

var TrafficLight = function() {
    this.greenRoad = 1;
};

/**
 * @param {number} carId
 * @param {number} roadId
 * @param {number} direction
 * @param {Function} turnGreen
 * @param {Function} crossCar
 * @return {void}
 */
TrafficLight.prototype.carArrived = function(carId, roadId, direction, turnGreen, crossCar) {
    if (roadId !== this.greenRoad) {
        turnGreen();
        this.greenRoad = roadId;
    }
    crossCar();
};
