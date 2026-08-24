// LeetCode 2528 - Maximize the Minimum Powered City
// https://leetcode.com/problems/maximize-the-minimum-powered-city/

/**
 * @param {number[]} stations
 * @param {number} r
 * @param {number} k
 * @return {number}
 */
var maxPower = function(stations, r, k) {
    const n = stations.length;
    const diff = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        const L = Math.max(0, i - r);
        const R = Math.min(n - 1, i + r);
        diff[L] += stations[i];
        diff[R + 1] -= stations[i];
    }
    const power = new Array(n);
    let cur = 0;
    for (let i = 0; i < n; i++) {
        cur += diff[i];
        power[i] = cur;
    }
    let lo = 0, hi = k;
    for (const p of power) if (p > hi) hi = p;
    hi += k;
    const ok = (x) => {
        const extra = new Array(n + 1).fill(0);
        let have = 0, used = 0;
        for (let i = 0; i < n; i++) {
            have += extra[i];
            const need = x - (power[i] + have);
            if (need > 0) {
                used += need;
                if (used > k) return false;
                have += need;
                const end = i + 2 * r;
                if (end + 1 <= n) extra[end + 1] -= need;
            }
        }
        return true;
    };
    while (lo < hi) {
        const mid = Math.floor((lo + hi + 1) / 2);
        if (ok(mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
};
