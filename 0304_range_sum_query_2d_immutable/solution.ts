// LeetCode 0304 - Range Sum Query 2D - Immutable
// https://leetcode.com/problems/range-sum-query-2d-immutable/

export class NumMatrix {
    private prefix: number[][];

    constructor(matrix: number[][]) {
        const rows = matrix.length;
        const cols = rows ? matrix[0].length : 0;
        this.prefix = Array.from({ length: rows + 1 }, () => Array(cols + 1).fill(0));
        for (let row = 0; row < rows; row += 1) {
            for (let col = 0; col < cols; col += 1) {
                this.prefix[row + 1][col + 1] = matrix[row][col]
                    + this.prefix[row][col + 1]
                    + this.prefix[row + 1][col]
                    - this.prefix[row][col];
            }
        }
    }

    sumRegion(row1: number, col1: number, row2: number, col2: number): number {
        return this.prefix[row2 + 1][col2 + 1]
            - this.prefix[row1][col2 + 1]
            - this.prefix[row2 + 1][col1]
            + this.prefix[row1][col1];
    }
}
