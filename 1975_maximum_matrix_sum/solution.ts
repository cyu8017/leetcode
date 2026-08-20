// LeetCode 1975 - Maximum Matrix Sum
// https://leetcode.com/problems/maximum-matrix-sum/

function maxMatrixSum(matrix: number[][]): number {
    let total = 0, neg = 0, mn = Infinity;
    for (const row of matrix) {
        for (const x of row) {
            if (x < 0) neg++;
            const ax = Math.abs(x);
            total += ax;
            mn = Math.min(mn, ax);
        }
    }
    return neg % 2 === 0 ? total : total - 2 * mn;
}
