// LeetCode 3148 - Maximum Difference Score in a Grid
// https://leetcode.com/problems/maximum-difference-score-in-a-grid/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxScore = function(grid) {
    const m = grid.length, n = grid[0].length;
    const INF = 1 << 30;
    const f = Array.from({ length: m }, () => new Array(n).fill(0));
    let ans = -INF;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            const x = grid[i][j];
            let mi = INF;
            if (i > 0) mi = Math.min(mi, f[i - 1][j]);
            if (j > 0) mi = Math.min(mi, f[i][j - 1]);
            ans = Math.max(ans, x - mi);
            f[i][j] = Math.min(x, mi);
        }
    }
    return ans;
};
