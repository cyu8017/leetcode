// LeetCode 0118 - Pascal's Triangle
// https://leetcode.com/problems/pascals-triangle/

export function generate(numRows: number): number[][] {
    const result: number[][] = [];
    for (let rowIndex = 0; rowIndex < numRows; rowIndex++) {
        const row: number[] = [];
        for (let column = 0; column <= rowIndex; column++) {
            if (column === 0 || column === rowIndex) {
                row.push(1);
            } else {
                row.push(result[rowIndex - 1][column - 1] + result[rowIndex - 1][column]);
            }
        }
        result.push(row);
    }
    return result;
}