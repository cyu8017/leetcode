"use strict";
// LeetCode 1727 - Largest Submatrix With Rearrangements
// https://leetcode.com/problems/largest-submatrix-with-rearrangements/
function largestSubmatrix(matrix) {
    const m = matrix.length;
    const n = matrix[0].length;
    const heights = new Array(n).fill(0);
    let best = 0;
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            heights[c] = matrix[r][c] ? heights[c] + 1 : 0;
        }
        const sorted = [...heights].sort((a, b) => b - a);
        for (let width = 1; width <= n; width++) {
            best = Math.max(best, width * sorted[width - 1]);
        }
    }
    return best;
}
