// LeetCode 2742 - Painting the Walls
// https://leetcode.com/problems/painting-the-walls/

/**
 * @param {number[]} cost
 * @param {number[]} time
 * @return {number}
 */
var paintWalls = function(cost, time) {
    const n = cost.length;
    const INF = Number.MAX_SAFE_INTEGER / 4;
    const dp = Array(n + 1).fill(INF);
    dp[0] = 0;
    for (let i = 0; i < n; i++) {
        for (let j = n; j >= 0; j--) {
            const nj = Math.min(n, j + time[i] + 1);
            if (dp[j] + cost[i] < dp[nj]) dp[nj] = dp[j] + cost[i];
        }
    }
    return dp[n];
};
