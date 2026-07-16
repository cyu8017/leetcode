// LeetCode 0543 - Diameter of Binary Tree
// https://leetcode.com/problems/diameter-of-binary-tree/

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
    diameterOfBinaryTree(root: TreeNode | null): number {
        let best = 0;
        const depth = (node: TreeNode | null): number => {
            if (!node) return 0;
            const left = depth(node.left);
            const right = depth(node.right);
            best = Math.max(best, left + right);
            return 1 + Math.max(left, right);
        };
        depth(root);
        return best;
    }
}
