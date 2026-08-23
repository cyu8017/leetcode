// LeetCode 0701 - Insert into a Binary Search Tree
// https://leetcode.com/problems/insert-into-a-binary-search-tree/

/**
 * @param {TreeNode} root
 * @param {number} val
 * @return {TreeNode}
 */
var insertIntoBST = function(root, val) {
    if (root === null) return new TreeNode(val);
    let node = root;
    while (true) {
        if (val < node.val) {
            if (node.left === null) { node.left = new TreeNode(val); break; }
            node = node.left;
        } else {
            if (node.right === null) { node.right = new TreeNode(val); break; }
            node = node.right;
        }
    }
    return root;
};
