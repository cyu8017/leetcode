// LeetCode 2196 - Create Binary Tree From Descriptions
// https://leetcode.com/problems/create-binary-tree-from-descriptions/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[][]} descriptions
 * @return {TreeNode}
 */
var createBinaryTree = function(descriptions) {
    const nodes = new Map();
    const child = new Set();
    for (const [p, c, isLeft] of descriptions) {
        if (!nodes.has(p)) nodes.set(p, new TreeNode(p));
        if (!nodes.has(c)) nodes.set(c, new TreeNode(c));
        if (isLeft === 1) nodes.get(p).left = nodes.get(c);
        else nodes.get(p).right = nodes.get(c);
        child.add(c);
    }
    for (const [k, v] of nodes)
        if (!child.has(k)) return v;
    return null;
};
