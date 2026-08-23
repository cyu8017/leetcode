// LeetCode 2732 - Find a Good Subset of the Matrix
// https://leetcode.com/problems/find-a-good-subset-of-the-matrix/

/**
 * @param {number[][]} grid
 * @return {number[]}
 */
var goodSubsetofBinaryMatrix = function(grid) {
    const n = grid[0].length;
    const first = new Map();
    for (let i = 0; i < grid.length; i++) {
        let mask = 0;
        for (let j = 0; j < n; j++) if (grid[i][j] === 1) mask |= 1 << j;
        if (mask === 0) return [i];
        for (const [pm, idx] of first) {
            if ((pm & mask) === 0) {
                return idx < i ? [idx, i] : [i, idx];
            }
        }
        if (!first.has(mask)) first.set(mask, i);
    }
    return [];
};
