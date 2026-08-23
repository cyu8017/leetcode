// LeetCode 0623 - Add One Row to Tree
// https://leetcode.com/problems/add-one-row-to-tree/

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
 * @param {number} val
 * @param {number} depth
 * @return {TreeNode}
 */
var addOneRow = function(root, val, depth) {
    if (depth === 1) return new TreeNode(val, root, null);
    const dfs = (node, current) => {
        if (node == null) return;
        if (current === depth - 1) {
            node.left = new TreeNode(val, node.left, null);
            node.right = new TreeNode(val, null, node.right);
            return;
        }
        dfs(node.left, current + 1);
        dfs(node.right, current + 1);
    };
    dfs(root, 1);
    return root;
};
