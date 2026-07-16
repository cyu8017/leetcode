// LeetCode 0114 - Flatten Binary Tree to Linked List
// https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

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

export function flatten(root: TreeNode | null): void {
    if (!root) {
        return;
    }

    flatten(root.left);
    flatten(root.right);

    if (root.left) {
        let tail = root.left;
        while (tail.right) {
            tail = tail.right;
        }
        tail.right = root.right;
        root.right = root.left;
        root.left = null;
    }
}