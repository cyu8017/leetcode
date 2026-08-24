// LeetCode 2482 - Difference Between Ones and Zeros in Row and Column
// https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

export function onesMinusZeros(grid: number[][]): number[][] {
    const m = grid.length, n = grid[0].length;
    const row = Array(m).fill(0), col = Array(n).fill(0);
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            row[i] += grid[i][j];
            col[j] += grid[i][j];
        }
    }
    const ans = Array.from({ length: m }, () => Array(n));
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            ans[i][j] = row[i] + col[j] - (m - row[i]) - (n - col[j]);
        }
    }
    return ans;
}
