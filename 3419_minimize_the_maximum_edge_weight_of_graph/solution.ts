// LeetCode 3419 - Minimize the Maximum Edge Weight of Graph
// https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph/

export function minMaxWeight(n: any, edges: any, threshold: any): any {
    const ok = (mid) => {
        const g = Array.from({ length: n }, () => []);
        for (const e of edges) {
            if (e[2] <= mid) g[e[1]].push(e[0]);
        }
        const vis = new Array(n).fill(false);
        const q = [0];
        vis[0] = true;
        let cnt = 1;
        while (q.length) {
            const u = q.shift();
            for (const v of g[u]) {
                if (!vis[v]) {
                    vis[v] = true;
                    cnt++;
                    q.push(v);
                }
            }
        }
        return cnt === n;
    };
    let lo = 1, hi = 1000001, ans = -1;
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (ok(mid)) {
            ans = mid;
            hi = mid;
        } else lo = mid + 1;
    }
    return ans;
}
