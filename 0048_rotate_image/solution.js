// LeetCode 0048 - Rotate Image
// https://leetcode.com/problems/rotate-image/

/**
 * @param {number[][]} matrix
 * @return {void}
 */
var rotate = function(matrix) {
    const n = matrix.length;

    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
        }
    }

    for (let i = 0; i < n; i++) {
        matrix[i].reverse();
    }
};
