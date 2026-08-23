// LeetCode 2378 - Choose Edges to Maximize Score in a Tree
// https://leetcode.com/problems/choose-edges-to-maximize-score-in-a-tree/

/**
 * @param {number[][]} edges
 * @return {number}
 */
var maxScore = function(edges) {
    const n = edges.length + 1;
    const g = Array.from({ length: n }, () => []);
    for (let i = 1; i < n; i++) {
        const p = edges[i - 1][0], w = edges[i - 1][1];
        g[p].push([i, w]);
        g[i].push([p, w]);
    }
    const dfs = (u, p) => {
        let base = 0;
        let bestGain = 0;
        for (const e of g[u]) {
            const to = e[0], w = e[1];
            if (to === p) continue;
            const child = dfs(to, u);
            base += child[0];
            const gain = child[1] + w - child[0];
            if (gain > bestGain) bestGain = gain;
        }
        return [base + bestGain, base];
    };
    return dfs(0, -1)[0];
};
