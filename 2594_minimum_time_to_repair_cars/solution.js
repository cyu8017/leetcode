// LeetCode 2594 - Minimum Time to Repair Cars
// https://leetcode.com/problems/minimum-time-to-repair-cars/

/**
 * @param {number[]} ranks
 * @param {number} cars
 * @return {number}
 */
var repairCars = function(ranks, cars) {
    let mn = Math.min(...ranks);
    let lo = 1, hi = mn * cars * cars;
    const ok = (t) => {
        let done = 0;
        for (const r of ranks) {
            let l = 0, h = cars;
            while (l < h) {
                const mid = Math.floor((l + h + 1) / 2);
                if (r * mid * mid <= t) l = mid;
                else h = mid - 1;
            }
            done += l;
            if (done >= cars) return true;
        }
        return done >= cars;
    };
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (ok(mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
};
