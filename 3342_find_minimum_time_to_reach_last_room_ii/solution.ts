// LeetCode 3342 - Find Minimum Time to Reach Last Room II
// https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/

export function minTimeToReach(moveTime: any): any {
    const m = moveTime.length, n = moveTime[0].length;
    const INF = 1 << 30;
    const dist = Array.from({length: m}, () => Array.from({length: n}, () => [INF, INF]));
    const pq = [[0, 0, 0, 0]];
    dist[0][0][0] = 0;
    const dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
    while (pq.length) {
        pq.sort((a, b) => a[0] - b[0]);
        const cur = pq.shift();
        const t = cur[0], r = cur[1], c = cur[2], parity = cur[3];
        if (t !== dist[r][c][parity]) continue;
        if (r === m - 1 && c === n - 1) return t;
        const cost = parity === 1 ? 2 : 1;
        for (const d of dirs) {
            const nr = r + d[0], nc = c + d[1];
            if (nr < 0 || nc < 0 || nr >= m || nc >= n) continue;
            const start = Math.max(t, moveTime[nr][nc]);
            const nt = start + cost;
            const np = 1 - parity;
            if (nt < dist[nr][nc][np]) {
                dist[nr][nc][np] = nt;
                pq.push([nt, nr, nc, np]);
            }
        }
    }
    return -1;
}
