// LeetCode 3244 - Shortest Distance After Road Addition Queries II
// https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/

export function shortestDistanceAfterQueries(n: any, queries: any): any {
    const nxt = new Array(n - 1);
    for (let i = 0; i < n - 1; i++) nxt[i] = i + 1;
    let cnt = n - 1;
    const ans = [];
    for (const q of queries) {
        const u = q[0], v = q[1];
        if (nxt[u] > 0 && nxt[u] < v) {
            let i = nxt[u];
            while (i < v) {
                cnt--;
                const ni = nxt[i];
                nxt[i] = 0;
                i = ni;
            }
            nxt[u] = v;
        }
        ans.push(cnt);
    }
    return ans;
}
