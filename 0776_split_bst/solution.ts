// LeetCode 0776 - Split BST
// https://leetcode.com/problems/split-bst/

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

export function splitBST(root: TreeNode | null, target: number): TreeNode | null[] {
    if (root === null) return [null, null];
    if (root.val <= target) {
        const parts = splitBST(root.right, target);
        root.right = parts[0];
        return [root, parts[1]];
    }
    const leftParts = splitBST(root.left, target);
    root.left = leftParts[1];
    return [leftParts[0], root];
}
