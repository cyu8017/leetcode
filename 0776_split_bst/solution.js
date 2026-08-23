// LeetCode 0776 - Split BST
// https://leetcode.com/problems/split-bst/

/**
 * @param {TreeNode} root
 * @param {number} target
 * @return {TreeNode[]}
 */
var splitBST = function(root, target) {
    if (root === null) return [null, null];
    if (root.val <= target) {
        const parts = splitBST(root.right, target);
        root.right = parts[0];
        return [root, parts[1]];
    }
    const leftParts = splitBST(root.left, target);
    root.left = leftParts[1];
    return [leftParts[0], root];
};
