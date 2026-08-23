// LeetCode 0655 - Print Binary Tree
// https://leetcode.com/problems/print-binary-tree/

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
 * @return {string[][]}
 */
var printTree = function(root) {
    const height = (node) => node == null ? -1 : 1 + Math.max(height(node.left), height(node.right));
    const h = height(root);
    const rows = h + 1;
    const cols = (1 << (h + 1)) - 1;
    const res = Array.from({ length: rows }, () => Array(cols).fill(""));
    const place = (node, r, c) => {
        if (node == null) return;
        res[r][c] = String(node.val);
        if (r === h) return;
        const offset = 1 << (h - r - 1);
        place(node.left, r + 1, c - offset);
        place(node.right, r + 1, c + offset);
    };
    place(root, 0, Math.floor((cols - 1) / 2));
    return res;
};
