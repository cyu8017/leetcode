// LeetCode 0119 - Pascal's Triangle II
// https://leetcode.com/problems/pascals-triangle-ii/

export function getRow(rowIndex: number): number[] {
    const row: number[] = [1];
    for (let size = 1; size <= rowIndex; size++) {
        row.push(1);
        for (let index = size - 1; index > 0; index--) {
            row[index] += row[index - 1];
        }
    }
    return row;
}