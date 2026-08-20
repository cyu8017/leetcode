// LeetCode 1572 - Matrix Diagonal Sum
// https://leetcode.com/problems/matrix-diagonal-sum/
// @ts-nocheck

function diagonalSum(mat: number[][]): number {
    const n = mat.length;
    let sum = 0;
    for (let i = 0; i < n; i++) sum += mat[i][i] + mat[i][n - 1 - i];
    if (n % 2) sum -= mat[Math.floor(n / 2)][Math.floor(n / 2)];
    return sum;
}
