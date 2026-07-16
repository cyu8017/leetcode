// LeetCode 0104 - Maximum Depth of Binary Tree
// https://leetcode.com/problems/maximum-depth-of-binary-tree/

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

export function maxDepth(root: TreeNode | null): number {
    if (!root) {
        return 0;
    }
    return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}