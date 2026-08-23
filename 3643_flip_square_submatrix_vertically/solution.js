// LeetCode 3643 - Flip Square Submatrix Vertically
// https://leetcode.com/problems/flip-square-submatrix-vertically/

var reverseSubmatrix = function(grid, x, y, k) {
    for (let i = x; i < x + Math.floor(k / 2); i++) {
        const i2 = x + k - 1 - (i - x);
        for (let j = y; j < y + k; j++) {
            const tmp = grid[i][j];
            grid[i][j] = grid[i2][j];
            grid[i2][j] = tmp;
        }
    }
    return grid;
};
