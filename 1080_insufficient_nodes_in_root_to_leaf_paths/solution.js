// LeetCode 1080 - Insufficient Nodes in Root to Leaf Paths
// https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/

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
 * @param {number} limit
 * @return {TreeNode}
 */
var sufficientSubset = function(root, limit) {
    function dfs(node, pathSum) {
        if (!node) return null;
        pathSum += node.val;
        if (!node.left && !node.right) {
            return pathSum >= limit ? node : null;
        }
        node.left = dfs(node.left, pathSum);
        node.right = dfs(node.right, pathSum);
        if (!node.left && !node.right) return null;
        return node;
    }
    return dfs(root, 0);
};
