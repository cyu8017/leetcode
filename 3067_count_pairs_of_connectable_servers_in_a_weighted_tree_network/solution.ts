// LeetCode 3067 - Count Pairs of Connectable Servers in a Weighted Tree Network
// https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/

export function countPairsOfConnectableServers(edges: number[][], signalSpeed: number): number[] {
    const n = edges.length + 1;
    const g = Array.from({ length: n }, () => []);
    for (const e of edges) {
        g[e[0]].push([e[1], e[2]]);
        g[e[1]].push([e[0], e[2]]);
    }
    const dfs = (a, fa, ws) => {
        let cnt = ws % signalSpeed === 0 ? 1 : 0;
        for (const [b, w] of g[a]) if (b !== fa) cnt += dfs(b, a, ws + w);
        return cnt;
    };
    const ans = new Array(n).fill(0);
    for (let a = 0; a < n; a++) {
        let s = 0;
        for (const [b, w] of g[a]) {
            const t = dfs(b, a, w);
            ans[a] += s * t;
            s += t;
        }
    }
    return ans;
}
