// LeetCode 0285 - Inorder Successor in BST
// https://leetcode.com/problems/inorder-successor-in-bst/

export class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;

    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = val ?? 0;
        this.left = left ?? null;
        this.right = right ?? null;
    }
}

export function inorderSuccessor(root: TreeNode | null, p: TreeNode): TreeNode | null {
    if (p.right) {
        let current: TreeNode | null = p.right;
        while (current.left) {
            current = current.left;
        }
        return current;
    }
    let successor: TreeNode | null = null;
    let current: TreeNode | null = root;
    while (current) {
        if (p.val < current.val) {
            successor = current;
            current = current.left;
        } else {
            current = current.right;
        }
    }
    return successor;
}
