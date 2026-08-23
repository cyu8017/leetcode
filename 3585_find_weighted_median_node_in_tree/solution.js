// LeetCode 3585 - Find Weighted Median Node in Tree
// https://leetcode.com/problems/find-weighted-median-node-in-tree/

var findMedian = function(n, edges, queries) {
    const g = Array.from({length: n}, () => []);
    for (const e of edges) {
        g[e[0]].push([e[1], e[2]]);
        g[e[1]].push([e[0], e[2]]);
    }
    const ans = new Array(queries.length);
    for (let qi = 0; qi < queries.length; qi++) {
        const u = queries[qi][0], v = queries[qi][1];
        const parent = new Array(n).fill(-2), pw = new Array(n).fill(0);
        parent[u] = -1;
        const q = [u];
        while (q.length) {
            const x = q.shift();
            if (x === v) break;
            for (const e of g[x]) {
                if (parent[e[0]] === -2) {
                    parent[e[0]] = x;
                    pw[e[0]] = e[1];
                    q.push(e[0]);
                }
            }
        }
        const nodes = [v];
        const weights = [];
        let cur = v;
        while (cur !== u) {
            weights.push(pw[cur]);
            cur = parent[cur];
            nodes.push(cur);
        }
        nodes.reverse();
        weights.reverse();
        let total = 0;
        for (const w of weights) total += w;
        const need = Math.floor((total + 1) / 2);
        let sum = 0, med = u;
        for (let i = 0; i < weights.length; i++) {
            sum += weights[i];
            med = nodes[i + 1];
            if (sum >= need) break;
        }
        ans[qi] = med;
    }
    return ans;
};
