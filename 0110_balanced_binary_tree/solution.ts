// LeetCode 0110 - Balanced Binary Tree
// https://leetcode.com/problems/balanced-binary-tree/

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

function height(node: TreeNode | null): number {
    if (!node) {
        return 0;
    }
    const left = height(node.left);
    if (left === -1) {
        return -1;
    }
    const right = height(node.right);
    if (right === -1) {
        return -1;
    }
    if (Math.abs(left - right) > 1) {
        return -1;
    }
    return 1 + Math.max(left, right);
}

export function isBalanced(root: TreeNode | null): boolean {
    return height(root) !== -1;
}
