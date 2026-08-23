// LeetCode 0637 - Average of Levels in Binary Tree
// https://leetcode.com/problems/average-of-levels-in-binary-tree/

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
 * @return {number[]}
 */
var averageOfLevels = function(root) {
    const result = [];
    if (root == null) return result;
    const queue = [root];
    while (queue.length) {
        const count = queue.length;
        let total = 0;
        for (let i = 0; i < count; ++i) {
            const node = queue.shift();
            total += node.val;
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
        result.push(total / count);
    }
    return result;
};
