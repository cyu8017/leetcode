// LeetCode 0897 - Increasing Order Search Tree
// https://leetcode.com/problems/increasing-order-search-tree/

function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}

/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var increasingBST = function(root) {
    const dummy = new TreeNode(0);
    let cur = dummy;
    const inorder = (node) => {
        if (!node) return;
        inorder(node.left);
        node.left = null;
        cur.right = node;
        cur = node;
        inorder(node.right);
    };
    inorder(root);
    return dummy.right;
};
