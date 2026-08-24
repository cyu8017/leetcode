// LeetCode 3070 - Count Submatrices with Top-Left Element and Sum Less Than k
// https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/

/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number}
 */
var countSubmatrices = function(grid, k) {
    const n = grid.length, m = grid[0].length;
    let ans = 0;
    const s = Array.from({ length: n + 1 }, () => new Array(m + 1).fill(0));
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + grid[i][j];
            if (s[i + 1][j + 1] <= k) ans++;
        }
    }
    return ans;
};
