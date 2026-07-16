// LeetCode 0059 - Spiral Matrix II
// https://leetcode.com/problems/spiral-matrix-ii/

/**
 * @param {number} n
 * @return {number[][]}
 */
var generateMatrix = function(n) {
    const matrix = Array.from({ length: n }, () => Array(n).fill(0));
    let top = 0;
    let bottom = n - 1;
    let left = 0;
    let right = n - 1;
    let num = 1;

    while (top <= bottom && left <= right) {
        for (let col = left; col <= right; col++) {
            matrix[top][col] = num;
            num += 1;
        }
        top += 1;

        for (let row = top; row <= bottom; row++) {
            matrix[row][right] = num;
            num += 1;
        }
        right -= 1;

        if (top <= bottom) {
            for (let col = right; col >= left; col--) {
                matrix[bottom][col] = num;
                num += 1;
            }
            bottom -= 1;
        }

        if (left <= right) {
            for (let row = bottom; row >= top; row--) {
                matrix[row][left] = num;
                num += 1;
            }
            left += 1;
        }
    }

    return matrix;
};
