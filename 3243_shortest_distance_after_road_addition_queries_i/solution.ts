// LeetCode 3243 - Shortest Distance After Road Addition Queries I
// https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/

export function shortestDistanceAfterQueries(n: any, queries: any): any {
    const g = Array.from({length: n}, () => []);
    for (let i = 0; i < n - 1; i++) g[i].push(i + 1);
    const bfs = () => {
        const q = [0];
        const vis = new Array(n).fill(false);
        vis[0] = true;
        for (let d = 0; ; d++) {
            let k = q.length;
            while (k-- > 0) {
                const u = q.shift();
                if (u === n - 1) return d;
                for (const v of g[u]) {
                    if (!vis[v]) { vis[v] = true; q.push(v); }
                }
            }
        }
    };
    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        g[queries[i][0]].push(queries[i][1]);
        ans[i] = bfs();
    }
    return ans;
}
