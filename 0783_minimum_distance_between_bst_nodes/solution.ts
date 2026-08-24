// LeetCode 0783 - Minimum Distance Between BST Nodes
// https://leetcode.com/problems/minimum-distance-between-bst-nodes/

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

export function minDiffInBST(root: TreeNode | null): number {
    let hasPrev = false, prev = 0, best = Number.MAX_SAFE_INTEGER;
    const inorder = (node) => {
        if (!node) return;
        inorder(node.left);
        if (hasPrev) best = Math.min(best, node.val - prev);
        prev = node.val;
        hasPrev = true;
        inorder(node.right);
    };
    inorder(root);
    return best;
}
