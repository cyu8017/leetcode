// LeetCode 1080 - Insufficient Nodes in Root to Leaf Paths
// https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/

class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = val ?? 0;
        this.left = left ?? null;
        this.right = right ?? null;
    }
}

function sufficientSubset(root: TreeNode | null, limit: number): TreeNode | null {
    function dfs(node: TreeNode | null, pathSum: number): TreeNode | null {
        if (!node) return null;
        pathSum += node.val;
        if (!node.left && !node.right) {
            return pathSum >= limit ? node : null;
        }
        node.left = dfs(node.left, pathSum);
        node.right = dfs(node.right, pathSum);
        if (!node.left && !node.right) return null;
        return node;
    }
    return dfs(root, 0);
}
