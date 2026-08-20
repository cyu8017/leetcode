"use strict";
// LeetCode 1329 - Sort The Matrix Diagonally
// https://leetcode.com/problems/sort-the-matrix-diagonally/
function diagonalSort(mat) {
    const diagonals = new Map();
    for (let r = 0; r < mat.length; r++) {
        for (let c = 0; c < mat[0].length; c++) {
            const key = r - c;
            if (!diagonals.has(key))
                diagonals.set(key, []);
            diagonals.get(key).push(mat[r][c]);
        }
    }
    for (const values of diagonals.values())
        values.sort((a, b) => b - a);
    for (let r = 0; r < mat.length; r++) {
        for (let c = 0; c < mat[0].length; c++) {
            mat[r][c] = diagonals.get(r - c).pop();
        }
    }
    return mat;
}
