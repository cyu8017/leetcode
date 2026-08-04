// LeetCode 1184 - Distance Between Bus Stops
// https://leetcode.com/problems/distance-between-bus-stops/

/**
 * @param {number[]} distance
 * @param {number} start
 * @param {number} destination
 * @return {number}
 */
var distanceBetweenBusStops = function(distance, start, destination) {
    if (start > destination) [start, destination] = [destination, start];
    let clockwise = 0, total = 0;
    for (let i = 0; i < distance.length; i++) {
        total += distance[i];
        if (i >= start && i < destination) clockwise += distance[i];
    }
    return Math.min(clockwise, total - clockwise);
};
