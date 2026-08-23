// LeetCode 4003 - Minimum Cost Path with Alternating Directions III
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-iii/

var minCost = function(m, n, penalty) {
    const INF = 2 ** 60;
    const dist = Array.from({length: m}, () => Array.from({length: n}, () => [INF, INF]));
    dist[0][0][1] = 1;
    const pq = [[1, 0, 0, 1]];
    const dirs = [[-1, 0], [0, 1], [0, -1], [1, 0]];
    while (pq.length) {
        pq.sort((a, b) => a[0] - b[0]);
        const cur = pq.shift();
        const d = cur[0], i = cur[1], j = cur[2], k = cur[3];
        if (i === m - 1 && j === n - 1) return d;
        if (d > dist[i][j][k]) continue;
        const p = penalty[i][j];
        let nd = d + p;
        if (nd < dist[i][j][k ^ 1]) {
            dist[i][j][k ^ 1] = nd;
            pq.push([nd, i, j, k ^ 1]);
        }
        for (let idx = 0; idx < 4; idx++) {
            const x = i + dirs[idx][0], y = j + dirs[idx][1];
            if (0 <= x && x < m && 0 <= y && y < n) {
                nd = d + ((x + 1) * (y + 1) + (((idx & 1) ^ k) * p));
                if (nd < dist[x][y][k ^ 1]) {
                    dist[x][y][k ^ 1] = nd;
                    pq.push([nd, x, y, k ^ 1]);
                }
            }
        }
    }
    return -1;
};
