// LeetCode 1605 - Find Valid Matrix Given Row and Column Sums
// https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/

/**
 * @param {number[]} rowSum
 * @param {number[]} colSum
 * @return {number[][]}
 */
var restoreMatrix = function(rowSum, colSum) {
    const ans = Array.from({ length: rowSum.length }, () => Array(colSum.length).fill(0));
    let i = 0, j = 0;
    while (i < rowSum.length && j < colSum.length) {
        const x = Math.min(rowSum[i], colSum[j]);
        ans[i][j] = x;
        rowSum[i] -= x;
        colSum[j] -= x;
        if (rowSum[i] === 0) i++;
        if (colSum[j] === 0) j++;
    }
    return ans;
};
