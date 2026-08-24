// LeetCode 2331 - Evaluate Boolean Binary Tree
// https://leetcode.com/problems/evaluate-boolean-binary-tree/

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

export function evaluateTree(root: TreeNode | null): boolean {
    if (root.left === null && root.right === null) return root.val === 1;
    const l = evaluateTree(root.left);
    const r = evaluateTree(root.right);
    if (root.val === 2) return l || r;
    return l && r;
}
