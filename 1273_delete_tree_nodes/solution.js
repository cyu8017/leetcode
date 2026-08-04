// LeetCode 1273 - Delete Tree Nodes
// https://leetcode.com/problems/delete-tree-nodes/

/**
 * @param {number} nodes
 * @param {number[]} parent
 * @param {number[]} value
 * @return {number}
 */
var deleteTreeNodes = function(nodes, parent, value) {
    const children = Array.from({ length: nodes }, () => []);
    for (let node = 1; node < nodes; node++) {
        children[parent[node]].push(node);
    }
    const dfs = (node) => {
        let total = value[node];
        let count = 1;
        for (const child of children[node]) {
            const [childSum, childCount] = dfs(child);
            total += childSum;
            count += childCount;
        }
        return [total, total === 0 ? 0 : count];
    };
    return dfs(0)[1];
};
