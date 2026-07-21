"use strict";
// LeetCode 1870 - Minimum Speed to Arrive on Time
// https://leetcode.com/problems/minimum-speed-to-arrive-on-time/
function minSpeedOnTime(dist, hour) {
    const n = dist.length;
    if (n - 1 >= hour)
        return -1;
    const canArrive = (speed) => {
        let time = 0;
        for (let i = 0; i < n - 1; i++) {
            time += Math.floor((dist[i] + speed - 1) / speed);
        }
        time += dist[n - 1] / speed;
        return time <= hour;
    };
    if (!canArrive(1e7))
        return -1;
    let lo = 1, hi = 1e7;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (canArrive(mid))
            hi = mid;
        else
            lo = mid + 1;
    }
    return lo;
}
