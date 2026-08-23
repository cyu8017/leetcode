// LeetCode 3786 - Total Sum Of Interaction Cost In Tree Groups
// https://leetcode.com/problems/total_sum_of_interaction_cost_in_tree_groups/

var interactionCost = function(n, edges, group) {
    const g = Array.from({length: n}, () => []);
    for (const e of edges) {
        g[e[0]].push(e[1]);
        g[e[1]].push(e[0]);
    }
    const total = new Array(21).fill(0);
    for (const x of group) total[x]++;
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
    const count = Array.from({length: n}, () => new Array(21).fill(0));
    let ans = 0;
    for (let i = n - 1; i >= 0; i--) {
        const u = order[i];
        count[u][group[u]]++;
        for (const v of g[u]) {
            if (parent[v] !== u) continue;
            for (let c = 1; c <= 20; c++) {
                const x = count[v][c];
                ans += x * (total[c] - x);
                count[u][c] += x;
            }
        }
    }
    return ans;
};
