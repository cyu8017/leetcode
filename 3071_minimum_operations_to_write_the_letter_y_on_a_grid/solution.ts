// LeetCode 3071 - Minimum Operations to Write the Letter Y on a Grid
// https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/

export function minimumOperationsToWriteY(grid: number[][]): number {
    const n = grid.length;
    const cnt1 = [0, 0, 0], cnt2 = [0, 0, 0];
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            const x = grid[i][j];
            const a = i === j && i <= Math.floor(n / 2);
            const b = i + j === n - 1 && i <= Math.floor(n / 2);
            const c = j === Math.floor(n / 2) && i >= Math.floor(n / 2);
            if (a || b || c) cnt1[x]++;
            else cnt2[x]++;
        }
    }
    let ans = n * n;
    for (let i = 0; i < 3; i++)
        for (let j = 0; j < 3; j++)
            if (i !== j) ans = Math.min(ans, n * n - cnt1[i] - cnt2[j]);
    return ans;
}
