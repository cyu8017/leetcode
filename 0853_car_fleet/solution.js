// LeetCode 0853 - Car Fleet
// https://leetcode.com/problems/car-fleet/

/**
 * @param {number} target
 * @param {number[]} position
 * @param {number[]} speed
 * @return {number}
 */
var carFleet = function(target, position, speed) {
    const n = position.length;
    const cars = [];
    for (let i = 0; i < n; i++) cars.push([position[i], speed[i]]);
    cars.sort((a, b) => b[0] - a[0]);
    let fleets = 0, maxTime = 0;
    for (const [pos, spd] of cars) {
        const time = (target - pos) / spd;
        if (time > maxTime) {
            fleets++;
            maxTime = time;
        }
    }
    return fleets;
};
