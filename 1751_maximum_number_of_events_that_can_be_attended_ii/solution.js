// LeetCode 1751 - Maximum Number of Events That Can Be Attended II
// https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/

/**
 * @param {number[][]} events
 * @param {number} k
 * @return {number}
 */
var maxValue = function(events, k) {
    events = events.slice().sort((a, b) => a[0] - b[0] || a[1] - b[1] || a[2] - b[2]);
    const n = events.length;
    const starts = events.map((e) => e[0]);

    const upperBound = (target) => {
        let lo = 0;
        let hi = n;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (starts[mid] <= target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    };

    const dp = Array.from({ length: k + 1 }, () => new Array(n + 1).fill(0));
    for (let i = n - 1; i >= 0; i--) {
        const j = upperBound(events[i][1]);
        for (let remain = 1; remain <= k; remain++) {
            dp[remain][i] = Math.max(dp[remain][i + 1], events[i][2] + dp[remain - 1][j]);
        }
    }
    return dp[k][0];
};
