// LeetCode 2319 - Check if Matrix Is X-Matrix
// https://leetcode.com/problems/check-if-matrix-is-x-matrix/

/**
 * @param {number[][]} grid
 * @return {boolean}
 */
var checkXMatrix = function(grid) {
    const n = grid.length;
    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < n; ++j) {
            const diag = (i === j || i + j === n - 1);
            if (diag) { if (grid[i][j] === 0) return false; }
            else if (grid[i][j] !== 0) return false;
        }
    }
    return true;
};
