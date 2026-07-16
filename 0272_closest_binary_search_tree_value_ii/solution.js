// LeetCode 0272 - Closest Binary Search Tree Value II
// https://leetcode.com/problems/closest-binary-search-tree-value-ii/

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
 * @param {number} target
 * @param {number} k
 * @return {number[]}
 */
var closestKValues = function(root, target, k) {
    const values = [];

    const inorder = (node) => {
        if (!node) {
            return;
        }
        inorder(node.left);
        values.push(node.val);
        inorder(node.right);
    };

    inorder(root);

    let lo = 0;
    let hi = values.length;
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (values[mid] < target) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }

    let left = lo - 1;
    let right = lo;
    const result = [];
    while (result.length < k) {
        if (
            right >= values.length ||
            (left >= 0 && Math.abs(values[left] - target) <= Math.abs(values[right] - target))
        ) {
            result.push(values[left]);
            left -= 1;
        } else {
            result.push(values[right]);
            right += 1;
        }
    }
    return result;
};
