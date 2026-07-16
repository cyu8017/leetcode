// LeetCode 0114 - Flatten Binary Tree to Linked List
// https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}

/**
 * @param {TreeNode} root
 * @return {void}
 */
var flatten = function(root) {
    if (!root) {
        return;
    }

    flatten(root.left);
    flatten(root.right);

    if (root.left) {
        let tail = root.left;
        while (tail.right) {
            tail = tail.right;
        }
        tail.right = root.right;
        root.right = root.left;
        root.left = null;
    }
};