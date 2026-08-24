// LeetCode 2304 - Minimum Path Cost in a Grid
// https://leetcode.com/problems/minimum-path-cost-in-a-grid/

/**
 * @param {number[][]} grid
 * @param {number[][]} moveCost
 * @return {number}
 */
var minPathCost = function(grid, moveCost) {
    const m = grid.length, n = grid[0].length;
    let dp = grid[0].slice();
    for (let r = 0; r < m - 1; ++r) {
        const next = Array(n).fill(Math.floor(2147483647 / 2));
        for (let c = 0; c < n; ++c) {
            const from = grid[r][c];
            for (let nc = 0; nc < n; ++nc) {
                next[nc] = Math.min(next[nc], dp[c] + moveCost[from][nc] + grid[r + 1][nc]);
            }
        }
        dp = next;
    }
    let ans = dp[0];
    for (let i = 1; i < n; i++) ans = Math.min(ans, dp[i]);
    return ans;
};
