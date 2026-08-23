// LeetCode 3341 - Find Minimum Time to Reach Last Room I
// https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/

var minTimeToReach = function(moveTime) {
    const m = moveTime.length, n = moveTime[0].length;
    const dist = Array.from({length: m}, () => new Array(n).fill(1 << 30));
    const h = [[0, 0, 0]];
    dist[0][0] = 0;
    const dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
    while (h.length) {
        h.sort((a, b) => a[0] - b[0]);
        const cur = h.shift();
        const t = cur[0], r = cur[1], c = cur[2];
        if (t !== dist[r][c]) continue;
        if (r === m - 1 && c === n - 1) return t;
        for (const d of dirs) {
            const nr = r + d[0], nc = c + d[1];
            if (nr < 0 || nc < 0 || nr >= m || nc >= n) continue;
            const start = Math.max(t, moveTime[nr][nc]);
            const nt = start + 1;
            if (nt < dist[nr][nc]) {
                dist[nr][nc] = nt;
                h.push([nt, nr, nc]);
            }
        }
    }
    return -1;
};
