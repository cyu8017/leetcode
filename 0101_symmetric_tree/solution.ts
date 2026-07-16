// LeetCode 0101 - Symmetric Tree
// https://leetcode.com/problems/symmetric-tree/

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

function mirrors(left: TreeNode | null, right: TreeNode | null): boolean {
    if (!left && !right) {
        return true;
    }
    if (!left || !right || left.val !== right.val) {
        return false;
    }
    return mirrors(left.left, right.right) && mirrors(left.right, right.left);
}

export function isSymmetric(root: TreeNode | null): boolean {
    if (!root) {
        return true;
    }
    return mirrors(root.left, root.right);
}
