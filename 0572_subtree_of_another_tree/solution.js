// LeetCode 0572 - Subtree of Another Tree
// https://leetcode.com/problems/subtree-of-another-tree/

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
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
var isSubtree = function(root, subRoot) {
    const same = (a, b) => {
        if (a == null || b == null) return a === b;
        return a.val === b.val && same(a.left, b.left) && same(a.right, b.right);
    };
    if (root == null) return false;
    return same(root, subRoot) || isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
};
