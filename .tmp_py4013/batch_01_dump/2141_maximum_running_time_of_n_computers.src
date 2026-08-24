// LeetCode 2141 - Maximum Running Time of N Computers
// https://leetcode.com/problems/maximum-running-time-of-n-computers/

/**
 * @param {number} n
 * @param {number[]} batteries
 * @return {number}
 */
var maxRunTime = function(n, batteries) {
    let sum = 0;
    for (const b of batteries) sum += b;
    let lo = 1, hi = Math.floor(sum / n);
    while (lo < hi) {
        const mid = Math.floor((lo + hi + 1) / 2);
        let need = 0;
        for (const b of batteries) need += Math.min(b, mid);
        if (need >= mid * n) lo = mid;
        else hi = mid - 1;
    }
    return lo;
};
