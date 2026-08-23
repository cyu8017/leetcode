// LeetCode 2583 - Kth Largest Sum in a Binary Tree
// https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

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
 * @param {number} k
 * @return {number}
 */
var kthLargestLevelSum = function(root, k) {
    if (!root) return -1;
    const sums = [];
    const q = [root];
    while (q.length) {
        const sz = q.length;
        let s = 0;
        for (let i = 0; i < sz; ++i) {
            const node = q.shift();
            s += node.val;
            if (node.left) q.push(node.left);
            if (node.right) q.push(node.right);
        }
        sums.push(s);
    }
    sums.sort((a, b) => b - a);
    if (k > sums.length) return -1;
    return sums[k - 1];
};
