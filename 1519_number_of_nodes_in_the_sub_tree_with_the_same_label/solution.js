// LeetCode 1519 - Number of Nodes in the Sub-Tree With the Same Label
// https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/

/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {string} labels
 * @return {number[]}
 */
var countSubTrees = function(n, edges, labels) {
    const graph = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) {
        graph[a].push(b);
        graph[b].push(a);
    }
    const answer = Array(n).fill(0);
    const dfs = (node, parent) => {
        const counts = Array(26).fill(0);
        const index = labels.charCodeAt(node) - 97;
        counts[index] = 1;
        for (const neighbor of graph[node]) {
            if (neighbor !== parent) {
                const child = dfs(neighbor, node);
                for (let i = 0; i < 26; i++) counts[i] += child[i];
            }
        }
        answer[node] = counts[index];
        return counts;
    };
    dfs(0, -1);
    return answer;
};
