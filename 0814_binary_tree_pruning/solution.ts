// LeetCode 0814 - Binary Tree Pruning
// https://leetcode.com/problems/binary-tree-pruning/

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

export function pruneTree(root: TreeNode | null): TreeNode | null {
    if (!root) return null;
    root.left = pruneTree(root.left);
    root.right = pruneTree(root.right);
    if (root.val === 0 && !root.left && !root.right) return null;
    return root;
}
