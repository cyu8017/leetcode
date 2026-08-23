// LeetCode 0700 - Search in a Binary Search Tree
// https://leetcode.com/problems/search-in-a-binary-search-tree/

/**
 * @param {TreeNode} root
 * @param {number} val
 * @return {TreeNode}
 */
var searchBST = function(root, val) {
    while (root !== null && root.val !== val) {
        root = val < root.val ? root.left : root.right;
    }
    return root;
};
