// LeetCode 2959 - Number of Possible Sets of Closing Branches
// https://leetcode.com/problems/number-of-possible-sets-of-closing-branches/

var numberOfSets = function(n, maxDistance, roads) {
    let ans = 0;
    for (let mask = 0; mask < (1 << n); mask++) {
        const dist = Array.from({length: n}, () => new Array(n).fill(1 << 29));
        for (let i = 0; i < n; i++) dist[i][i] = 0;
        for (const r of roads) {
            const u = r[0], v = r[1], w = r[2];
            if ((mask & (1 << u)) !== 0 && (mask & (1 << v)) !== 0) {
                if (w < dist[u][v]) {
                    dist[u][v] = w;
                    dist[v][u] = w;
                }
            }
        }
        for (let k = 0; k < n; k++) {
            if ((mask & (1 << k)) === 0) continue;
            for (let i = 0; i < n; i++) {
                if ((mask & (1 << i)) === 0) continue;
                for (let j = 0; j < n; j++) {
                    if ((mask & (1 << j)) === 0) continue;
                    if (dist[i][k] + dist[k][j] < dist[i][j])
                        dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
        let ok = true;
        for (let i = 0; i < n && ok; i++) {
            if ((mask & (1 << i)) === 0) continue;
            for (let j = 0; j < n; j++) {
                if ((mask & (1 << j)) === 0) continue;
                if (dist[i][j] > maxDistance) { ok = false; break; }
            }
        }
        if (ok) ans++;
    }
    return ans;
};
