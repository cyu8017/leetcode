"use strict";
// LeetCode 1886 - Determine Whether Matrix Can Be Obtained By Rotation
// https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/
function findRotation(mat, target) {
    let current = mat;
    const equal = (a, b) => {
        for (let i = 0; i < a.length; i++) {
            for (let j = 0; j < a[i].length; j++) {
                if (a[i][j] !== b[i][j])
                    return false;
            }
        }
        return true;
    };
    for (let rot = 0; rot < 4; rot++) {
        if (equal(current, target))
            return true;
        const n = current.length;
        current = Array.from({ length: n }, (_, col) => Array.from({ length: n }, (_, row) => current[n - 1 - row][col]));
    }
    return false;
}
