// LeetCode 0054 - Spiral Matrix
// https://leetcode.com/problems/spiral-matrix/

/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    if (matrix.length === 0) {
        return [];
    }

    let top = 0;
    let bottom = matrix.length - 1;
    let left = 0;
    let right = matrix[0].length - 1;
    const result = [];

    while (top <= bottom && left <= right) {
        for (let col = left; col <= right; col++) {
            result.push(matrix[top][col]);
        }
        top += 1;

        for (let row = top; row <= bottom; row++) {
            result.push(matrix[row][right]);
        }
        right -= 1;

        if (top <= bottom) {
            for (let col = right; col >= left; col--) {
                result.push(matrix[bottom][col]);
            }
            bottom -= 1;
        }

        if (left <= right) {
            for (let row = bottom; row >= top; row--) {
                result.push(matrix[row][left]);
            }
            left += 1;
        }
    }

    return result;
};
