// LeetCode 0783 - Minimum Distance Between BST Nodes
// https://leetcode.com/problems/minimum-distance-between-bst-nodes/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var minDiffInBST = function(root) {
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
};
