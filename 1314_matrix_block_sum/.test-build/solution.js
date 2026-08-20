"use strict";
// LeetCode 1314 - Matrix Block Sum
// https://leetcode.com/problems/matrix-block-sum/
function matrixBlockSum(mat, k) {
    const m = mat.length, n = mat[0].length;
    const prefix = Array.from({ length: m + 1 }, (), any), any;
    Array(n + 1).fill(0);
    ;
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            prefix[r + 1][c + 1] = mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c];
        }
    }
    const answer = Array.from({ length: m }, (), any), any;
    Array(n).fill(0);
    ;
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            const r1 = Math.max(0, r - k), c1 = Math.max(0, c - k);
            const r2 = Math.min(m, r + k + 1), c2 = Math.min(n, c + k + 1);
            answer[r][c] = prefix[r2][c2] - prefix[r1][c2] - prefix[r2][c1] + prefix[r1][c1];
        }
    }
    return answer;
}
