// LeetCode 2463 - Minimum Total Distance Traveled
// https://leetcode.com/problems/minimum-total-distance-traveled/

/**
 * @param {number[]} robot
 * @param {number[][]} factory
 * @return {number}
 */
var minimumTotalDistance = function(robot, factory) {
    const robots = robot.slice().sort((a, b) => a - b);
    factory = factory.slice().sort((a, b) => a[0] - b[0]);
    const m = robots.length;
    const pos = [];
    for (const f of factory) {
        for (let c = 0; c < f[1]; c++) pos.push(f[0]);
    }
    const n = pos.length;
    const INF = Number.MAX_SAFE_INTEGER / 4;
    const dp = Array.from({ length: m + 1 }, () => Array(n + 1).fill(INF));
    for (let j = 0; j <= n; j++) dp[0][j] = 0;
    for (let i = 1; i <= m; i++) {
        for (let j = i; j <= n; j++) {
            dp[i][j] = dp[i][j - 1];
            let diff = robots[i - 1] - pos[j - 1];
            if (diff < 0) diff = -diff;
            if (dp[i - 1][j - 1] + diff < dp[i][j]) dp[i][j] = dp[i - 1][j - 1] + diff;
        }
    }
    return dp[m][n];
};
