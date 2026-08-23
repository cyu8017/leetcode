// LeetCode 2332 - The Latest Time to Catch a Bus
// https://leetcode.com/problems/the-latest-time-to-catch-a-bus/

/**
 * @param {number[]} buses
 * @param {number[]} passengers
 * @param {number} capacity
 * @return {number}
 */
var latestTimeCatchTheBus = function(buses, passengers, capacity) {
    buses.sort((a, b) => a - b);
    passengers.sort((a, b) => a - b);
    let pos = 0;
    for (let bi = 0; bi < buses.length; bi++) {
        const bus = buses[bi];
        let cap = capacity;
        while (cap > 0 && pos < passengers.length && passengers[pos] <= bus) {
            pos++;
            cap--;
        }
        if (bi === buses.length - 1) {
            let cand = bus;
            if (cap === 0) cand = passengers[pos - 1];
            const taken = new Set(passengers);
            while (taken.has(cand)) cand--;
            return cand;
        }
    }
    return -1;
};
