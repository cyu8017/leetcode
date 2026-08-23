// LeetCode 3367 - Maximize Sum of Weights after Edge Removals
// https://leetcode.com/problems/maximize-sum-of-weights-after-edge-removals/

var maximizeSumOfWeights = function(edges, k) {
    const n = edges.length + 1;
    const g = Array.from({length: n}, () => []);
    for (const e of edges) {
        g[e[0]].push([e[1], e[2]]);
        g[e[1]].push([e[0], e[2]]);
    }
    const dfs = (u, p) => {
        let base = 0;
        const gains = [];
        for (const e of g[u]) {
            const to = e[0], w = e[1];
            if (to === p) continue;
            const child = dfs(to, u);
            base += child[1];
            const gain = child[0] + w - child[1];
            if (gain > 0) gains.push(gain);
        }
        gains.sort((a, b) => b - a);
        let withP = base, without = base;
        for (let i = 0; i < gains.length && i < k - 1; i++) withP += gains[i];
        for (let i = 0; i < gains.length && i < k; i++) without += gains[i];
        return [withP, without];
    };
    return dfs(0, -1)[1];
};
