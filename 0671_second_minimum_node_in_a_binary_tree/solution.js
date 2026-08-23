// LeetCode 0671 - Second Minimum Node In a Binary Tree
// https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

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
var findSecondMinimumValue = function(root) {
    if (root == null) return -1;
    let ans = -1;
    const rootVal = root.val;
    const dfs = (node) => {
        if (node == null) return;
        if (node.val > rootVal) {
            if (ans === -1 || node.val < ans) ans = node.val;
            return;
        }
        dfs(node.left);
        dfs(node.right);
    };
    dfs(root);
    return ans;
};
