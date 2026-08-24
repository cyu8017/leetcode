// LeetCode 2187 - Minimum Time to Complete Trips
// https://leetcode.com/problems/minimum-time-to-complete-trips/

/**
 * @param {number[]} time
 * @param {number} totalTrips
 * @return {number}
 */
var minimumTime = function(time, totalTrips) {
    let mn = time[0];
    for (const t of time) mn = Math.min(mn, t);
    let lo = 1, hi = mn * totalTrips;
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        let trips = 0;
        let ok = false;
        for (const t of time) {
            trips += Math.floor(mid / t);
            if (trips >= totalTrips) { ok = true; break; }
        }
        if (ok) hi = mid;
        else lo = mid + 1;
    }
    return lo;
};
