// LeetCode 0240 - Search a 2D Matrix II
// https://leetcode.com/problems/search-a-2d-matrix-ii/

/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    if (!matrix.length || !matrix[0].length) {
        return false;
    }
    let row = 0;
    let col = matrix[0].length - 1;
    while (row < matrix.length && col >= 0) {
        const value = matrix[row][col];
        if (value === target) {
            return true;
        }
        if (value > target) {
            col--;
        } else {
            row++;
        }
    }
    return false;
};
