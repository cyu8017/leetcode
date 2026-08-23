// LeetCode 0652 - Find Duplicate Subtrees
// https://leetcode.com/problems/find-duplicate-subtrees/

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
 * @return {TreeNode[]}
 */
var findDuplicateSubtrees = function(root) {
    const counts = new Map();
    const result = [];
    const serialize = (node) => {
        if (node == null) return "#";
        const key = node.val + "," + serialize(node.left) + "," + serialize(node.right);
        const count = (counts.get(key) || 0) + 1;
        counts.set(key, count);
        if (count === 2) result.push(node);
        return key;
    };
    serialize(root);
    return result;
};
