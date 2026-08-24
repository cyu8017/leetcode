// LeetCode 2973 - Find Number of Coins to Place in Tree Nodes
// https://leetcode.com/problems/find-number-of-coins-to-place-in-tree-nodes/

export function placedCoins(edges: any, cost: any): any {
    const n = cost.length;
    const g = Array.from({length: n}, () => []);
    for (const e of edges) {
        g[e[0]].push(e[1]);
        g[e[1]].push(e[0]);
    }
    const ans = new Array(n).fill(0);
    function dfs(u: any, p: any): any {
        let vals = [cost[u]];
        for (const v of g[u]) {
            if (v === p) continue;
            vals = vals.concat(dfs(v, u));
        }
        vals.sort((a, b) => a - b);
        if (vals.length < 3) {
            ans[u] = 1;
        } else {
            const m = vals.length;
            const cand1 = vals[m - 1] * vals[m - 2] * vals[m - 3];
            const cand2 = vals[0] * vals[1] * vals[m - 1];
            let best = Math.max(cand1, cand2);
            if (best < 0) best = 0;
            ans[u] = best;
        }
        if (vals.length <= 5) return vals;
        return [vals[0], vals[1], vals[vals.length - 3], vals[vals.length - 2], vals[vals.length - 1]];
    }    dfs(0, -1);
    return ans;
}
