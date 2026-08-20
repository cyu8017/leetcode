"use strict";
// LeetCode 1380 - Lucky Numbers In A Matrix
// https://leetcode.com/problems/lucky-numbers-in-a-matrix/
function luckyNumbers(matrix) {
    const mins = new Set(matrix.map((r) => Math.min(...r)));
    const cols = matrix[0].length;
    const maxs = new Set();
    for (let c = 0; c < cols; c++) {
        let mx = -Infinity;
        for (let r = 0; r < matrix.length; r++)
            mx = Math.max(mx, matrix[r][c]);
        maxs.add(mx);
    }
    return [...mins].filter((x) => maxs.has(x));
}
