// LeetCode 1260 - Shift 2D Grid
// https://leetcode.com/problems/shift-2d-grid/

/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number[][]}
 */
var shiftGrid = function(grid, k) {
    const m = grid.length, n = grid[0].length;
    let flat = grid.flat();
    k %= flat.length;
    if (k) flat = flat.slice(-k).concat(flat.slice(0, -k));
    const answer = [];
    for (let i = 0; i < m; i++) answer.push(flat.slice(i * n, (i + 1) * n));
    return answer;
};
