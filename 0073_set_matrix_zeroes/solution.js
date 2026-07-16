// LeetCode 0073 - Set Matrix Zeroes
// https://leetcode.com/problems/set-matrix-zeroes/

/**
 * @param {number[][]} matrix
 * @return {void}
 */
var setZeroes = function(matrix) {
    const rows = matrix.length;
    const cols = matrix[0].length;
    const firstRowZero = matrix[0].some((value) => value === 0);
    const firstColZero = matrix.some((row) => row[0] === 0);

    for (let i = 1; i < rows; i++) {
        for (let j = 1; j < cols; j++) {
            if (matrix[i][j] === 0) {
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }
        }
    }

    for (let i = 1; i < rows; i++) {
        for (let j = 1; j < cols; j++) {
            if (matrix[i][0] === 0 || matrix[0][j] === 0) {
                matrix[i][j] = 0;
            }
        }
    }

    if (firstRowZero) {
        for (let j = 0; j < cols; j++) {
            matrix[0][j] = 0;
        }
    }
    if (firstColZero) {
        for (let i = 0; i < rows; i++) {
            matrix[i][0] = 0;
        }
    }
};
