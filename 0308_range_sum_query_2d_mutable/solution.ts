// LeetCode 0308 - Range Sum Query 2D - Mutable
// https://leetcode.com/problems/range-sum-query-2d-mutable/

export class NumMatrix {
    private matrix: number[][];
    private rows: number;
    private cols: number;
    private tree: number[][];
    private add: (row: number, col: number, delta: number) => void;

    constructor(matrix: number[][]) {
        this.matrix = matrix;
        this.rows = matrix.length;
        this.cols = this.rows ? matrix[0].length : 0;
        this.tree = Array.from({ length: this.rows + 1 }, () => Array(this.cols + 1).fill(0));
        this.add = (row: number, col: number, delta: number) => {
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

    update(row: number, col: number, val: number): void {
        const delta = val - this.matrix[row][col];
        this.matrix[row][col] = val;
        this.add(row + 1, col + 1, delta);
    }

    sumRegion(row1: number, col1: number, row2: number, col2: number): number {
        const prefix = (row: number, col: number): number => {
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
