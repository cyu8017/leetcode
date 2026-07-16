// LeetCode 0074 - Search a 2D Matrix
// https://leetcode.com/problems/search-a-2d-matrix/

export function searchMatrix(matrix: number[][], target: number): boolean {
    let row = 0;
    let col = matrix[0].length - 1;

    while (row < matrix.length && col >= 0) {
        if (matrix[row][col] === target) {
            return true;
        }
        if (matrix[row][col] > target) {
            col--;
        } else {
            row++;
        }
    }

    return false;
}
