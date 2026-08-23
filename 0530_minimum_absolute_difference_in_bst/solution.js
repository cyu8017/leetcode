// LeetCode 0530 - Minimum Absolute Difference in BST
// https://leetcode.com/problems/minimum-absolute-difference-in-bst/

class TreeNode {
    constructor(val = 0, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    getMinimumDifference(root) {
        let previous = null;
        let best = Infinity;
        const inorder = (node) => {
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

module.exports = { Solution, TreeNode };
