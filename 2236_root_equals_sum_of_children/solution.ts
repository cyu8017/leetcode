// LeetCode 2236 - Root Equals Sum of Children
// https://leetcode.com/problems/root-equals-sum-of-children/

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

export function checkTree(root: TreeNode | null): boolean {
    return root.val === root.left.val + root.right.val;
}
