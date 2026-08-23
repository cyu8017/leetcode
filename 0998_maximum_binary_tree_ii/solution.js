// LeetCode 0998 - Maximum Binary Tree II
// https://leetcode.com/problems/maximum-binary-tree-ii/

/**
 * @param {TreeNode} root
 * @param {number} val
 * @return {TreeNode}
 */
var insertIntoMaxTree = function(root, val) {
    if (!root || val > root.val) {
        const node = new TreeNode(val);
        node.left = root;
        return node;
    }
    root.right = insertIntoMaxTree(root.right, val);
    return root;
};
