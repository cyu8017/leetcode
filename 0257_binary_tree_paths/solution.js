// LeetCode 0257 - Binary Tree Paths
// https://leetcode.com/problems/binary-tree-paths/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}

/**
 * @param {TreeNode} root
 * @return {string[]}
 */
var binaryTreePaths = function(root) {
    const result = [];

    const dfs = (node, path) => {
        if (!node) {
            return;
        }
        path.push(String(node.val));
        if (!node.left && !node.right) {
            result.push(path.join('->'));
        } else {
            dfs(node.left, path);
            dfs(node.right, path);
        }
        path.pop();
    };

    dfs(root, []);
    return result;
};
