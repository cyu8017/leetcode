// LeetCode 2050 - Parallel Courses III
// https://leetcode.com/problems/parallel-courses-iii/

export function minimumTime(n: number, relations: number[][], time: number[]): number {
    const g = Array.from({length: n + 1}, () => []);
    const indeg = new Array(n + 1).fill(0);
    const dist = new Array(n + 1).fill(0);
    for (const e of relations) { g[e[0]].push(e[1]); indeg[e[1]]++; }
    const q = [];
    for (let i = 1; i <= n; i++) {
        dist[i] = time[i - 1];
        if (indeg[i] === 0) q.push(i);
    }
    while (q.length) {
        const u = q.shift();
        for (const v of g[u]) {
            dist[v] = Math.max(dist[v], dist[u] + time[v - 1]);
            if (--indeg[v] === 0) q.push(v);
        }
    }
    let ans = 0;
    for (let i = 1; i <= n; i++) ans = Math.max(ans, dist[i]);
    return ans;
}
