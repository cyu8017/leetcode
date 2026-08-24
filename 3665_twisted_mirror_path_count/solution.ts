// LeetCode 3665 - Twisted Mirror Path Count
// https://leetcode.com/problems/twisted-mirror-path-count/

export function uniquePaths(grid: any): any {
    const MOD = 1000000007;
    const m = grid.length, n = grid[0].length;
    const nextCell = (i, j, di, dj) => {
        let ni = i + di, nj = j + dj;
        while (ni >= 0 && nj >= 0 && ni < m && nj < n && grid[ni][nj] === 1) {
            if (dj === 1) { di = 1; dj = 0; }
            else { di = 0; dj = 1; }
            ni += di;
            nj += dj;
        }
        if (ni < 0 || nj < 0 || ni >= m || nj >= n) return null;
        return [ni, nj];
    };
    const dp = Array.from({length: m}, () => new Array(n).fill(0));
    if (grid[0][0] === 1) return 0;
    dp[0][0] = 1;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1 || dp[i][j] === 0) continue;
            const a = nextCell(i, j, 0, 1);
            if (a) dp[a[0]][a[1]] = (dp[a[0]][a[1]] + dp[i][j]) % MOD;
            const b = nextCell(i, j, 1, 0);
            if (b) dp[b[0]][b[1]] = (dp[b[0]][b[1]] + dp[i][j]) % MOD;
        }
    }
    return dp[m - 1][n - 1];
}
