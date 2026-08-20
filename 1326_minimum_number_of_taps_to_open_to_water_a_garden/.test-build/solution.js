"use strict";
// LeetCode 1326 - Minimum Number Of Taps To Open To Water A Garden
// https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/
function minTaps(n, ranges) {
    const farthest = Array(n + 1).fill(0);
    for (let center = 0; center < ranges.length; center++) {
        const left = Math.max(0, center - ranges[center]);
        const right = Math.min(n, center + ranges[center]);
        farthest[left] = Math.max(farthest[left], right);
    }
    let taps = 0, end = 0, reach = 0;
    for (let position = 0; position < n; position++) {
        reach = Math.max(reach, farthest[position]);
        if (position === end) {
            if (reach <= position)
                return -1;
            taps++;
            end = reach;
        }
    }
    return taps;
}
