// LeetCode 0965 - Univalued Binary Tree
// https://leetcode.com/problems/univalued-binary-tree/

function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}

/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isUnivalTree = function(root) {
    if (!root) return true;
    const dfs = (node, v) => {
        if (!node) return true;
        if (node.val !== v) return false;
        return dfs(node.left, v) && dfs(node.right, v);
    };
    return dfs(root, root.val);
};
