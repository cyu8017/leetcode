// LeetCode 1895 - Largest Magic Square
// https://leetcode.com/problems/largest-magic-square/

function largestMagicSquare(grid: number[][]): number {
    const rows = grid.length, cols = grid[0].length;
    const rowPrefix = Array.from({ length: rows }, () => new Array(cols + 1).fill(0));
    const colPrefix = Array.from({ length: cols }, () => new Array(rows + 1).fill(0));
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            rowPrefix[i][j + 1] = rowPrefix[i][j] + grid[i][j];
            colPrefix[j][i + 1] = colPrefix[j][i] + grid[i][j];
        }
    }
    const rowSum = (row: number, colStart: number, colEnd: number) => rowPrefix[row][colEnd + 1] - rowPrefix[row][colStart];
    const colSum = (col: number, rowStart: number, rowEnd: number) => colPrefix[col][rowEnd + 1] - colPrefix[col][rowStart];
    const isMagic = (rowStart: number, colStart: number, size: number) => {
        const target = rowSum(rowStart, colStart, colStart + size - 1);
        for (let row = rowStart; row < rowStart + size; row++) {
            if (rowSum(row, colStart, colStart + size - 1) !== target) return false;
        }
        for (let col = colStart; col < colStart + size; col++) {
            if (colSum(col, rowStart, rowStart + size - 1) !== target) return false;
        }
        let diag1 = 0, diag2 = 0;
        for (let offset = 0; offset < size; offset++) {
            diag1 += grid[rowStart + offset][colStart + offset];
            diag2 += grid[rowStart + offset][colStart + size - 1 - offset];
        }
        return diag1 === target && diag2 === target;
    };
    for (let size = Math.min(rows, cols); size > 0; size--) {
        for (let rowStart = 0; rowStart <= rows - size; rowStart++) {
            for (let colStart = 0; colStart <= cols - size; colStart++) {
                if (isMagic(rowStart, colStart, size)) return size;
            }
        }
    }
    return 1;
}
