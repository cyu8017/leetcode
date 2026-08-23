// LeetCode 3989 - Maximum Consistent Columns in a Grid
// https://leetcode.com/problems/maximum-consistent-columns-in-a-grid/
var maxConsistentColumns = function(grid, limit) {
        let m = grid.length;
        let n = grid[0].length;
        let dp = new Array(n).fill(0);
        let ans = 1;
        for (let j = 0; j < n; j++) {
            dp[j] = 1;
            for (let i = 0; i < j; i++) {
                if (dp[i] + 1 <= dp[j]) continue;
                let ok = true;
                for (let r = 0; r < m; r++) {
                    let d = Math.abs(grid[r][j] - grid[r][i]);
                    if (d > limit) { ok = false; break; }
                }
                if (ok) dp[j] = dp[i] + 1;
            }
            if (dp[j] > ans) ans = dp[j];
        }
        return ans;
    
};
