// LeetCode 0235 - Lowest Common Ancestor of a Binary Search Tree
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

export class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;

    constructor(val = 0, left: TreeNode | null = null, right: TreeNode | null = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

export function lowestCommonAncestor(
    root: TreeNode | null,
    p: TreeNode,
    q: TreeNode
): TreeNode | null {
    let current = root;
    while (current) {
        if (p.val < current.val && q.val < current.val) {
            current = current.left;
        } else if (p.val > current.val && q.val > current.val) {
            current = current.right;
        } else {
            return current;
        }
    }
    return current;
}
