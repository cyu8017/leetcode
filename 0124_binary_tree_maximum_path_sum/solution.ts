// LeetCode 0124 - Binary Tree Maximum Path Sum
// https://leetcode.com/problems/binary-tree-maximum-path-sum/

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

export function maxPathSum(root: TreeNode | null): number {
    let best = -Infinity;

    const gain = (node: TreeNode | null): number => {
        if (!node) {
            return 0;
        }

        const left = Math.max(gain(node.left), 0);
        const right = Math.max(gain(node.right), 0);
        best = Math.max(best, node.val + left + right);
        return node.val + Math.max(left, right);
    };

    gain(root);
    return best;
}