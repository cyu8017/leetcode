// LeetCode 1273 - Delete Tree Nodes
// https://leetcode.com/problems/delete-tree-nodes/

function deleteTreeNodes(nodes: number, parent: number[], value: number[]): number {
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
}
