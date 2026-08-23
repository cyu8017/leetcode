// LeetCode 0815 - Bus Routes
// https://leetcode.com/problems/bus-routes/

/**
 * @param {number[][]} routes
 * @param {number} source
 * @param {number} target
 * @return {number}
 */
var numBusesToDestination = function(routes, source, target) {
    if (source === target) return 0;
    const stopToBuses = new Map();
    for (let bus = 0; bus < routes.length; bus++) {
        for (const stop of routes[bus]) {
            if (!stopToBuses.has(stop)) stopToBuses.set(stop, []);
            stopToBuses.get(stop).push(bus);
        }
    }
    const queue = [[source, 0]];
    const seenStops = new Set([source]);
    const seenBuses = new Set();
    while (queue.length) {
        const [stop, busesTaken] = queue.shift();
        for (const bus of (stopToBuses.get(stop) || [])) {
            if (seenBuses.has(bus)) continue;
            seenBuses.add(bus);
            for (const nxt of routes[bus]) {
                if (nxt === target) return busesTaken + 1;
                if (!seenStops.has(nxt)) {
                    seenStops.add(nxt);
                    queue.push([nxt, busesTaken + 1]);
                }
            }
        }
    }
    return -1;
};
