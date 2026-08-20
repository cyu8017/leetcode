// LeetCode 1110 - Delete Nodes And Return Forest
// https://leetcode.com/problems/delete-nodes-and-return-forest/

class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val = 0, left: TreeNode | null = null, right: TreeNode | null = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

function delNodes(root: TreeNode | null, to_delete: number[]): TreeNode[] {
    const deleteSet = new Set(to_delete);
    const forest = [];
    const dfs = (node, isRoot) => {
        if (!node) return null;
        const removed = deleteSet.has(node.val);
        if (isRoot && !removed) forest.push(node);
        node.left = dfs(node.left, removed);
        node.right = dfs(node.right, removed);
        return removed ? null : node;
    };
    dfs(root, true);
    return forest;
}
