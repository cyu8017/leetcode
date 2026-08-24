// LeetCode 3286 - Find a Safe Walk Through a Grid
// https://leetcode.com/problems/find-a-safe-walk-through-a-grid/

export function findSafeWalk(grid: any, health: any): any {
    const m = grid.length, n = grid[0].length;
    const vis = Array.from({length: m}, () => new Array(n).fill(-1));
    let qh = health - grid[0][0];
    if (qh <= 0) return false;
    const q = [[0, 0, qh]];
    vis[0][0] = qh;
    const dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
    while (q.length) {
        const cur = q.shift();
        if (cur[0] === m - 1 && cur[1] === n - 1) return true;
        for (const d of dirs) {
            const nr = cur[0] + d[0], nc = cur[1] + d[1];
            if (nr < 0 || nc < 0 || nr >= m || nc >= n) continue;
            const nh = cur[2] - grid[nr][nc];
            if (nh <= 0) continue;
            if (nh > vis[nr][nc]) {
                vis[nr][nc] = nh;
                q.push([nr, nc, nh]);
            }
        }
    }
    return false;
}
