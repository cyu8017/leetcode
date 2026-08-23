// LeetCode 2328 - Number of Increasing Paths in a Grid
// https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var countPaths = function(grid) {
    const MOD = 1000000007;
    const m = grid.length, n = grid[0].length;
    const dp = Array.from({ length: m }, () => Array(n).fill(0));
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    const dfs = (r, c) => {
        if (dp[r][c] !== 0) return dp[r][c];
        let res = 1;
        for (const d of dirs) {
            const nr = r + d[0], nc = c + d[1];
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] > grid[r][c])
                res = (res + dfs(nr, nc)) % MOD;
        }
        dp[r][c] = res;
        return res;
    };
    let ans = 0;
    for (let i = 0; i < m; ++i)
        for (let j = 0; j < n; ++j)
            ans = (ans + dfs(i, j)) % MOD;
    return ans;
};
