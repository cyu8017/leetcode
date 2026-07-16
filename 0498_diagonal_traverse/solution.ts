// LeetCode 0498 - Diagonal Traverse
// https://leetcode.com/problems/diagonal-traverse/

export class Solution {
    findDiagonalOrder(mat: number[][]): number[] {
        if (!mat.length || !mat[0].length) return [];
        const rows = mat.length;
        const cols = mat[0].length;
        const result: number[] = [];
        let row = 0;
        let col = 0;
        let upward = true;

        for (let step = 0; step < rows * cols; step += 1) {
            result.push(mat[row][col]);
            if (upward) {
                if (col === cols - 1) {
                    row += 1;
                    upward = false;
                } else if (row === 0) {
                    col += 1;
                    upward = false;
                } else {
                    row -= 1;
                    col += 1;
                }
            } else if (row === rows - 1) {
                col += 1;
                upward = true;
            } else if (col === 0) {
                row += 1;
                upward = true;
            } else {
                row += 1;
                col -= 1;
            }
        }
        return result;
    }
}
