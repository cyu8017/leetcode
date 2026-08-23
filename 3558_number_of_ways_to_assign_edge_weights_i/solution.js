// LeetCode 3558 - Number of Ways to Assign Edge Weights I
// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/

var assignEdgeWeights = function(edges) {
    const mod = 1000000007;
    const n = edges.length + 1;
    const g = Array.from({length: n + 1}, () => []);
    for (const e of edges) {
        g[e[0]].push(e[1]);
        g[e[1]].push(e[0]);
    }
    function dfs(i, fa) {
        let res = 0;
        for (const j of g[i]) if (j !== fa) res = Math.max(res, dfs(j, i) + 1);
        return res;
    }
    function pow2(exp) {
        let a = 2n, res = 1n, m = BigInt(mod);
        while (exp > 0) {
            if (exp & 1) res = res * a % m;
            a = a * a % m;
            exp >>= 1;
        }
        return Number(res);
    }
    return pow2(dfs(1, 0) - 1);
};
