// LeetCode 2684 - Maximum Number of Moves in a Grid
// https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/

export function maxMoves(grid: any): any {
    const m = grid.length, n = grid[0].length;
    let dp = new Array(m).fill(0);
    for (let c = n - 2; c >= 0; c--) {
        const ndp = new Array(m).fill(0);
        for (let r = 0; r < m; r++) {
            let best = 0;
            for (let dr = -1; dr <= 1; dr++) {
                const nr = r + dr;
                if (nr >= 0 && nr < m && grid[nr][c + 1] > grid[r][c])
                    best = Math.max(best, 1 + dp[nr]);
            }
            ndp[r] = best;
        }
        dp = ndp;
    }
    return Math.max(...dp);
}
