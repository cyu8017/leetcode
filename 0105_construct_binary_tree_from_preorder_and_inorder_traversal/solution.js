// LeetCode 0105 - Construct Binary Tree from Preorder and Inorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

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
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function(preorder, inorder) {
    var index = {};
    for (var i = 0; i < inorder.length; i++) {
        index[inorder[i]] = i;
    }
    var preIndex = 0;

    function build(left, right) {
        if (left > right) {
            return null;
        }
        var rootVal = preorder[preIndex++];
        var mid = index[rootVal];
        var root = new TreeNode(rootVal);
        root.left = build(left, mid - 1);
        root.right = build(mid + 1, right);
        return root;
    }

    return build(0, inorder.length - 1);
};