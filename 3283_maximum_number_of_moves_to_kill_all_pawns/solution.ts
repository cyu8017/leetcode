// LeetCode 3283 - Maximum Number of Moves to Kill All Pawns
// https://leetcode.com/problems/maximum-number-of-moves-to-kill-all-pawns/

export function maxMoves(kx: any, ky: any, positions: any): any {
    const DIRS = [[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]];
    const knightDist = (x, y, pts) => {
        const np = pts.length;
        const ans = new Array(np).fill(-1);
        const vis = Array.from({length: 50}, () => new Array(50).fill(false));
        const q = [[x, y, 0]];
        vis[x][y] = true;
        const need = new Map();
        for (let i = 0; i < np; i++) {
            const key = (BigInt(pts[i][0]) << 32n) | BigInt(pts[i][1] >>> 0);
            if (!need.has(key)) need.set(key, []);
            need.get(key).push(i);
        }
        let found = 0;
        while (q.length && found < np) {
            const cur = q.shift();
            const key = (BigInt(cur[0]) << 32n) | BigInt(cur[1] >>> 0);
            const idxs = need.get(key);
            if (idxs) {
                for (const i of idxs) {
                    if (ans[i] === -1) { ans[i] = cur[2]; found++; }
                }
            }
            for (const d of DIRS) {
                const nx = cur[0] + d[0], ny = cur[1] + d[1];
                if (nx < 0 || ny < 0 || nx >= 50 || ny >= 50 || vis[nx][ny]) continue;
                vis[nx][ny] = true;
                q.push([nx, ny, cur[2] + 1]);
            }
        }
        return ans;
    };
    const n = positions.length;
    const pts = Array.from({length: n + 1}, () => [0, 0]);
    pts[0][0] = kx; pts[0][1] = ky;
    for (let i = 0; i < n; i++) { pts[i + 1][0] = positions[i][0]; pts[i + 1][1] = positions[i][1]; }
    const dist = [];
    for (let i = 0; i <= n; i++) dist[i] = knightDist(pts[i][0], pts[i][1], pts);
    const N = 1 << n;
    const memo = Array.from({length: N}, () => new Array(n + 1).fill(-1));
    const dfs = (mask, cur, turn) => {
        if (mask === N - 1) return 0;
        if (memo[mask][cur] !== -1) return memo[mask][cur];
        let best = turn === 0 ? -(1 << 30) : (1 << 30);
        for (let i = 0; i < n; i++) {
            if ((mask & (1 << i)) !== 0) continue;
            const d = dist[cur][i + 1];
            const v = d + dfs(mask | (1 << i), i + 1, 1 - turn);
            if (turn === 0) { if (v > best) best = v; }
            else if (v < best) best = v;
        }
        return (memo[mask][cur] = best);
    };
    return dfs(0, 0, 0);
}
