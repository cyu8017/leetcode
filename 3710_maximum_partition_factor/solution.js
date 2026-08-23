// LeetCode 3710 - Maximum Partition Factor
// https://leetcode.com/problems/maximum-partition-factor/

var maxPartitionFactor = function(points) {
    const n = points.length;
    if (n === 2) return 0;
    const dist = (i, j) => Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1]);
    const ok = (d) => {
        const g = Array.from({length: n}, () => []);
        for (let i = 0; i < n; i++) {
            for (let j = i + 1; j < n; j++) {
                if (dist(i, j) < d) {
                    g[i].push(j);
                    g[j].push(i);
                }
            }
        }
        const color = new Array(n).fill(-1);
        for (let i = 0; i < n; i++) {
            if (color[i] !== -1) continue;
            const q = [i];
            color[i] = 0;
            while (q.length) {
                const u = q.shift();
                for (const v of g[u]) {
                    if (color[v] === -1) {
                        color[v] = color[u] ^ 1;
                        q.push(v);
                    } else if (color[v] === color[u]) return false;
                }
            }
        }
        return true;
    };
    let lo = 0, hi = 0;
    for (let i = 0; i < n; i++)
        for (let j = i + 1; j < n; j++)
            hi = Math.max(hi, dist(i, j));
    while (lo < hi) {
        const mid = Math.floor((lo + hi + 1) / 2);
        if (ok(mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
};
