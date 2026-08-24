// LeetCode 3651 - Minimum Cost Path with Teleportations
// https://leetcode.com/problems/minimum-cost-path-with-teleportations/

export function minCost(grid: any, k: any): any {
    const m = grid.length, n = grid[0].length;
    const inf = 536870911;
    const f = Array.from({length: k + 1}, () =>
        Array.from({length: m}, () => new Array(n).fill(inf)));
    f[0][0][0] = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (i > 0) f[0][i][j] = Math.min(f[0][i][j], f[0][i - 1][j] + grid[i][j]);
            if (j > 0) f[0][i][j] = Math.min(f[0][i][j], f[0][i][j - 1] + grid[i][j]);
        }
    }
    const g = new Map();
    for (let i = 0; i < m; i++)
        for (let j = 0; j < n; j++) {
            if (!g.has(grid[i][j])) g.set(grid[i][j], []);
            g.get(grid[i][j]).push([i, j]);
        }
    const keys = [...g.keys()].sort((a, b) => b - a);
    for (let t = 1; t <= k; t++) {
        let mn = inf;
        for (const key of keys) {
            const pos = g.get(key);
            for (const p of pos) mn = Math.min(mn, f[t - 1][p[0]][p[1]]);
            for (const p of pos) f[t][p[0]][p[1]] = mn;
        }
        for (let i = 0; i < m; i++) {
            for (let j = 0; j < n; j++) {
                if (i > 0) f[t][i][j] = Math.min(f[t][i][j], f[t][i - 1][j] + grid[i][j]);
                if (j > 0) f[t][i][j] = Math.min(f[t][i][j], f[t][i][j - 1] + grid[i][j]);
            }
        }
    }
    let ans = inf;
    for (let t = 0; t <= k; t++) ans = Math.min(ans, f[t][m - 1][n - 1]);
    return ans;
}
