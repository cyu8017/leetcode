// LeetCode 0106 - Construct Binary Tree from Inorder and Postorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

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
 * @param {number[]} inorder
 * @param {number[]} postorder
 * @return {TreeNode}
 */
var buildTree = function(inorder, postorder) {
    var index = {};
    for (var i = 0; i < inorder.length; i++) {
        index[inorder[i]] = i;
    }
    var postIndex = postorder.length - 1;

    function build(left, right) {
        if (left > right) {
            return null;
        }
        var rootVal = postorder[postIndex--];
        var mid = index[rootVal];
        var root = new TreeNode(rootVal);
        root.right = build(mid + 1, right);
        root.left = build(left, mid - 1);
        return root;
    }

    return build(0, inorder.length - 1);
};