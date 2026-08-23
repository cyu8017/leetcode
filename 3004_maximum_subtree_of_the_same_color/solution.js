// LeetCode 3004 - Maximum Subtree of the Same Color
// https://leetcode.com/problems/maximum-subtree-of-the-same-color/

var maximumSubtreeSize = function(edges, colors) {
    const n = edges.length + 1;
    const g = Array.from({length: n}, () => []);
    for (const e of edges) {
        g[e[0]].push(e[1]);
        g[e[1]].push(e[0]);
    }
    const size = new Array(n).fill(0);
    let ans = 0;
    function dfs(a, fa) {
        size[a] = 1;
        let ok = true;
        for (const b of g[a]) {
            if (b !== fa) {
                const t = dfs(b, a);
                ok = ok && t && colors[a] === colors[b];
                size[a] += size[b];
            }
        }
        if (ok) ans = Math.max(ans, size[a]);
        return ok;
    }
    dfs(0, -1);
    return ans;
};
