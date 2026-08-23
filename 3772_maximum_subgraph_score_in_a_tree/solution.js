// LeetCode 3772 - Maximum Subgraph Score In A Tree
// https://leetcode.com/problems/maximum_subgraph_score_in_a_tree/

var maxSubgraphScore = function(n, edges, good) {
    const g = Array.from({length: n}, () => []);
    for (const e of edges) {
        g[e[0]].push(e[1]);
        g[e[1]].push(e[0]);
    }
    const parent = new Array(n).fill(-2);
    parent[0] = -1;
    const order = [0];
    for (let i = 0; i < order.length; i++) {
        const u = order[i];
        for (const v of g[u]) {
            if (parent[v] === -2) {
                parent[v] = u;
                order.push(v);
            }
        }
    }
    const down = new Array(n);
    for (let i = n - 1; i >= 0; i--) {
        const u = order[i];
        down[u] = 2 * good[u] - 1;
        for (const v of g[u]) {
            if (parent[v] === u && down[v] > 0) down[u] += down[v];
        }
    }
    const ans = down.slice();
    for (const u of order) {
        for (const v of g[u]) {
            if (parent[v] === u) {
                let outside = ans[u];
                if (down[v] > 0) outside -= down[v];
                ans[v] = down[v];
                if (outside > 0) ans[v] += outside;
            }
        }
    }
    return ans;
};
