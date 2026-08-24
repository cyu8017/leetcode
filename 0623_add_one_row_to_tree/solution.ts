// LeetCode 0623 - Add One Row to Tree
// https://leetcode.com/problems/add-one-row-to-tree/

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

export function addOneRow(root: TreeNode | null, val: number, depth: number): TreeNode | null {
    if (depth === 1) return new TreeNode(val, root, null);
    const dfs = (node, current) => {
        if (node == null) return;
        if (current === depth - 1) {
            node.left = new TreeNode(val, node.left, null);
            node.right = new TreeNode(val, null, node.right);
            return;
        }
        dfs(node.left, current + 1);
        dfs(node.right, current + 1);
    };
    dfs(root, 1);
    return root;
}
