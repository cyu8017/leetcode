// LeetCode 0113 - Path Sum II
// https://leetcode.com/problems/path-sum-ii/

function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}

/**
 * @param {TreeNode} root
 * @param {number} targetSum
 * @return {number[][]}
 */
var pathSum = function(root, targetSum) {
    const result = [];

    const visit = function(node, remaining, path) {
        if (!node) {
            return;
        }
        path.push(node.val);
        if (!node.left && !node.right && remaining === node.val) {
            result.push([...path]);
        } else {
            visit(node.left, remaining - node.val, path);
            visit(node.right, remaining - node.val, path);
        }
        path.pop();
    };

    visit(root, targetSum, []);
    return result;
};