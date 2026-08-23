// LeetCode 2008 - Maximum Earnings From Taxi
// https://leetcode.com/problems/maximum-earnings-from-taxi/

/**
 * @param {number} n
 * @param {number[][]} rides
 * @return {number}
 */
var maxTaxiEarnings = function(n, rides) {
    rides.sort((a, b) => a[1] - b[1]);
    const m = rides.length;
    const ends = rides.map(r => r[1]);
    const dp = new Array(m + 1).fill(0);
    for (let i = 0; i < m; i++) {
        const [start, end, tip] = rides[i];
        const earn = end - start + tip;
        let lo = 0, hi = m;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (ends[mid] <= start) lo = mid + 1;
            else hi = mid;
        }
        dp[i + 1] = Math.max(dp[i], earn + dp[lo]);
    }
    return dp[m];
};
