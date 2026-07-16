// LeetCode 0304 - Range Sum Query 2D - Immutable
// https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix {
    /**
     * @param {number[][]} matrix
     */
    constructor(matrix) {
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

    /**
     * @param {number} row1
     * @param {number} col1
     * @param {number} row2
     * @param {number} col2
     * @return {number}
     */
    sumRegion(row1, col1, row2, col2) {
        return this.prefix[row2 + 1][col2 + 1]
            - this.prefix[row1][col2 + 1]
            - this.prefix[row2 + 1][col1]
            + this.prefix[row1][col1];
    }
}

module.exports = { NumMatrix };
