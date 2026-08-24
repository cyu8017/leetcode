// LeetCode 3122 - Minimum Number of Operations to Satisfy Conditions
// https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/

export function minimumOperations(grid: number[][]): number {
    const m = grid.length, n = grid[0].length;
    const INF = 1 << 29;
    const f = Array.from({ length: n }, () => new Array(10).fill(INF));
    for (let i = 0; i < n; i++) {
        const cnt = new Array(10).fill(0);
        for (let j = 0; j < m; j++) cnt[grid[j][i]]++;
        if (i === 0) {
            for (let j = 0; j < 10; j++) f[i][j] = m - cnt[j];
        } else {
            for (let j = 0; j < 10; j++) {
                for (let k = 0; k < 10; k++) {
                    if (j !== k) f[i][j] = Math.min(f[i][j], f[i - 1][k] + m - cnt[j]);
                }
            }
        }
    }
    let ans = INF;
    for (let j = 0; j < 10; j++) ans = Math.min(ans, f[n - 1][j]);
    return ans;
}
