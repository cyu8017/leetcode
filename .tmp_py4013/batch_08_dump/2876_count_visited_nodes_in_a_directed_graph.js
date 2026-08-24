// LeetCode 2876 - Count Visited Nodes in a Directed Graph
// https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/

/**
 * @param {number[]} edgesList
 * @return {number[]}
 */
var countVisitedNodes = function(edgesList) {
    const n = edgesList.length;
    const edges = edgesList.slice();
    const ans = Array(n).fill(0);
    const state = Array(n).fill(0);
    const stack = [];
    const dfs = (u) => {
        state[u] = 1;
        stack.push(u);
        const v = edges[u];
        if (state[v] === 0) dfs(v);
        else if (state[v] === 1) {
            let idx = stack.length - 1;
            while (stack[idx] !== v) idx--;
            const cyc = stack.length - idx;
            for (let i = idx; i < stack.length; i++) ans[stack[i]] = cyc;
        }
        if (ans[u] === 0) ans[u] = ans[edges[u]] + 1;
        state[u] = 2;
        stack.pop();
    };
    for (let i = 0; i < n; i++) if (state[i] === 0) dfs(i);
    return ans;
};
