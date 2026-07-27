// LeetCode 1660 - Correct a Binary Tree
// https://leetcode.com/problems/correct-a-binary-tree/

/**
 * @param {object} root
 * @return {object}
 */
var correctBinaryTree = function(root) {
    const seen = new Set();
    const dfs = (node) => {
        if (!node) return null;
        if (node.right && seen.has(node.right)) return null;
        seen.add(node);
        node.right = dfs(node.right);
        node.left = dfs(node.left);
        return node;
    };
    return dfs(root);
};
