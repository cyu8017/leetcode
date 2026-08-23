// LeetCode 3590 - Kth Smallest Path XOR Sum
// https://leetcode.com/problems/kth-smallest-path-xor-sum/

var kthSmallest = function(par, vals, queries) {
    const n = par.length;
    const g = Array.from({length: n}, () => []);
    for (let i = 1; i < n; i++) g[par[i]].push(i);
    const xorPath = new Array(n).fill(0);
    function dfs(u) {
        xorPath[u] ^= vals[u];
        for (const v of g[u]) {
            xorPath[v] = xorPath[u];
            dfs(v);
        }
    }
    dfs(0);
    const inT = new Array(n).fill(0), outT = new Array(n).fill(0);
    const order = [];
    function dfs2(u) {
        inT[u] = order.length;
        order.push(xorPath[u]);
        for (const v of g[u]) dfs2(v);
        outT[u] = order.length;
    }
    dfs2(0);
    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        const u = queries[i][0], k = queries[i][1];
        const sub = order.slice(inT[u], outT[u]).sort((a, b) => a - b);
        const uniq = [];
        for (const x of sub) if (uniq.length === 0 || uniq[uniq.length - 1] !== x) uniq.push(x);
        ans[i] = k > uniq.length ? -1 : uniq[k - 1];
    }
    return ans;
};
