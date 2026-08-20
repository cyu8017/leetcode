// LeetCode 1184 - Distance Between Bus Stops
// https://leetcode.com/problems/distance-between-bus-stops/

function distanceBetweenBusStops(distance: number[], start: number, destination: number): number {
    if (start > destination) [start, destination] = [destination, start];
    let clockwise = 0, total = 0;
    for (let i = 0; i < distance.length; i++) {
        total += distance[i];
        if (i >= start && i < destination) clockwise += distance[i];
    }
    return Math.min(clockwise, total - clockwise);
}
