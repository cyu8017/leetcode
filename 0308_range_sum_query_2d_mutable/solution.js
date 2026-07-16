// LeetCode 0308 - Range Sum Query 2D - Mutable
// https://leetcode.com/problems/range-sum-query-2d-mutable/

class NumMatrix {
    /**
     * @param {number[][]} matrix
     */
    constructor(matrix) {
        this.matrix = matrix;
        this.rows = matrix.length;
        this.cols = this.rows ? matrix[0].length : 0;
        this.tree = Array.from({ length: this.rows + 1 }, () => Array(this.cols + 1).fill(0));
        this.add = (row, col, delta) => {
            let rowIndex = row;
            while (rowIndex <= this.rows) {
                let colIndex = col;
                while (colIndex <= this.cols) {
                    this.tree[rowIndex][colIndex] += delta;
                    colIndex += colIndex & -colIndex;
                }
                rowIndex += rowIndex & -rowIndex;
            }
        };
        for (let row = 0; row < this.rows; row += 1) {
            for (let col = 0; col < this.cols; col += 1) {
                this.add(row + 1, col + 1, matrix[row][col]);
            }
        }
    }

    /**
     * @param {number} row
     * @param {number} col
     * @param {number} val
     * @return {void}
     */
    update(row, col, val) {
        const delta = val - this.matrix[row][col];
        this.matrix[row][col] = val;
        this.add(row + 1, col + 1, delta);
    }

    /**
     * @param {number} row1
     * @param {number} col1
     * @param {number} row2
     * @param {number} col2
     * @return {number}
     */
    sumRegion(row1, col1, row2, col2) {
        const prefix = (row, col) => {
            let total = 0;
            let rowIndex = row;
            while (rowIndex > 0) {
                let colIndex = col;
                while (colIndex > 0) {
                    total += this.tree[rowIndex][colIndex];
                    colIndex -= colIndex & -colIndex;
                }
                rowIndex -= rowIndex & -rowIndex;
            }
            return total;
        };
        return prefix(row2 + 1, col2 + 1) - prefix(row1, col2 + 1) - prefix(row2 + 1, col1) + prefix(row1, col1);
    }
}

module.exports = { NumMatrix };
