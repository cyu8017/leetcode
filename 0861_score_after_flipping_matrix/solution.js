// LeetCode 0861 - Score After Flipping Matrix
// https://leetcode.com/problems/score-after-flipping-matrix/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var matrixScore = function(grid) {
    const m = grid.length, n = grid[0].length;
    for (const row of grid) {
        if (row[0] === 0) {
            for (let j = 0; j < n; j++) row[j] ^= 1;
        }
    }
    let ans = m * (1 << (n - 1));
    for (let j = 1; j < n; j++) {
        let ones = 0;
        for (let i = 0; i < m; i++) ones += grid[i][j];
        ans += Math.max(ones, m - ones) * (1 << (n - 1 - j));
    }
    return ans;
};
