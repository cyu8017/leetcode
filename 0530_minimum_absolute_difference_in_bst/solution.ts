// LeetCode 0530 - Minimum Absolute Difference in BST
// https://leetcode.com/problems/minimum-absolute-difference-in-bst/

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

export class Solution {
    getMinimumDifference(root: TreeNode | null): number {
        let previous: number | null = null;
        let best = Infinity;
        const inorder = (node: TreeNode | null): void => {
            if (!node) return;
            inorder(node.left);
            if (previous !== null) best = Math.min(best, node.val - previous);
            previous = node.val;
            inorder(node.right);
        };
        inorder(root);
        return best;
    }
}
