// LeetCode 2258 - Escape the Spreading Fire
// https://leetcode.com/problems/escape-the-spreading-fire/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var maximumMinutes = function(grid) {
    const m = grid.length, n = grid[0].length;
    const inf = 1000000000;
    const fire = Array.from({length: m}, () => new Array(n).fill(inf));
    const q = [];
    for (let i = 0; i < m; i++)
        for (let j = 0; j < n; j++)
            if (grid[i][j] === 1) { fire[i][j] = 0; q.push([i, j]); }
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    while (q.length) {
        const [r, c] = q.shift();
        for (const d of dirs) {
            const nr = r + d[0], nc = c + d[1];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] === 2 || fire[nr][nc] !== inf) continue;
            fire[nr][nc] = fire[r][c] + 1;
            q.push([nr, nc]);
        }
    }
    const can = (wait) => {
        if (wait >= fire[0][0]) return false;
        const vis = Array.from({length: m}, () => new Array(n).fill(false));
        const qq = [[0, 0, wait]];
        vis[0][0] = true;
        while (qq.length) {
            const [r, c, t] = qq.shift();
            for (const d of dirs) {
                const nr = r + d[0], nc = c + d[1], nt = t + 1;
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] === 2 || vis[nr][nc]) continue;
                if (nr === m - 1 && nc === n - 1) {
                    if (nt <= fire[nr][nc]) return true;
                    continue;
                }
                if (nt >= fire[nr][nc]) continue;
                vis[nr][nc] = true;
                qq.push([nr, nc, nt]);
            }
        }
        return false;
    };
    let lo = 0, hi = m * n + 10, ans = -1;
    while (lo <= hi) {
        const mid = (lo + hi) >> 1;
        if (can(mid)) { ans = mid; lo = mid + 1; }
        else hi = mid - 1;
    }
    if (ans >= m * n) return inf;
    return ans;
};
