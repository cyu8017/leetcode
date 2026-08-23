// LeetCode 0103 - Binary Tree Zigzag Level Order Traversal
// https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

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
 * @return {number[][]}
 */
var zigzagLevelOrder = function(root) {
    if (!root) {
        return [];
    }

    var result = [];
    var queue = [root];
    var leftToRight = true;

    while (queue.length > 0) {
        var size = queue.length;
        var level = [];
        for (var i = 0; i < size; i++) {
            var node = queue.shift();
            level.push(node.val);
            if (node.left) {
                queue.push(node.left);
            }
            if (node.right) {
                queue.push(node.right);
            }
        }
        if (!leftToRight) {
            level.reverse();
        }
        result.push(level);
        leftToRight = !leftToRight;
    }

    return result;
};
