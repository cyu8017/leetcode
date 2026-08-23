// LeetCode 2088 - Count Fertile Pyramids in a Land
// https://leetcode.com/problems/count-fertile-pyramids-in-a-land/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var countPyramids = function(grid) {
    const count = (g) => {
        const m = g.length, n = g[0].length;
        const dp = g.map(row => row.slice());
        let ans = 0;
        for (let i = m - 2; i >= 0; i--) {
            for (let j = 1; j < n - 1; j++) {
                if (g[i][j] === 1) {
                    dp[i][j] = 1 + Math.min(dp[i + 1][j - 1], Math.min(dp[i + 1][j], dp[i + 1][j + 1]));
                    ans += dp[i][j] - 1;
                }
            }
        }
        return ans;
    };
    let ans = count(grid);
    const m = grid.length;
    const rev = Array.from({length: m}, (_, i) => grid[m - 1 - i]);
    return ans + count(rev);
};
