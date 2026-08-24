// LeetCode 2492 - Minimum Score of a Path Between Two Cities
// https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

export function minScore(n: number, roads: number[][]): number {
    const g = Array.from({ length: n + 1 }, () => []);
    for (const r of roads) {
        g[r[0]].push([r[1], r[2]]);
        g[r[1]].push([r[0], r[2]]);
    }
    const vis = Array(n + 1).fill(false);
    let ans = 1 << 30;
    const q = [1];
    vis[1] = true;
    while (q.length) {
        const u = q.shift();
        for (const [v, w] of g[u]) {
            if (w < ans) ans = w;
            if (!vis[v]) {
                vis[v] = true;
                q.push(v);
            }
        }
    }
    return ans;
}
