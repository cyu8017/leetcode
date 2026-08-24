// LeetCode 0572 - Subtree of Another Tree
// https://leetcode.com/problems/subtree-of-another-tree/

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

export function isSubtree(root: TreeNode | null, subRoot: TreeNode | null): boolean {
    const same = (a, b) => {
        if (a == null || b == null) return a === b;
        return a.val === b.val && same(a.left, b.left) && same(a.right, b.right);
    };
    if (root == null) return false;
    return same(root, subRoot) || isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
}
