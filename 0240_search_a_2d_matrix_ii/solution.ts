// LeetCode 0240 - Search a 2D Matrix II
// https://leetcode.com/problems/search-a-2d-matrix-ii/

export function searchMatrix(matrix: number[][], target: number): boolean {
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
}
