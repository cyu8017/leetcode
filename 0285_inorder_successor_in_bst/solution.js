// LeetCode 0285 - Inorder Successor in BST
// https://leetcode.com/problems/inorder-successor-in-bst/

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @return {TreeNode|null}
 */
var inorderSuccessor = function(root, p) {
    if (p.right) {
        let current = p.right;
        while (current.left) {
            current = current.left;
        }
        return current;
    }
    let successor = null;
    let current = root;
    while (current) {
        if (p.val < current.val) {
            successor = current;
            current = current.left;
        } else {
            current = current.right;
        }
    }
    return successor;
};
