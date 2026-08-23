// LeetCode 0865 - Smallest Subtree with all the Deepest Nodes
// https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var subtreeWithAllDeepest = function(root) {
    const dfs = (node) => {
        if (!node) return { depth: 0, node: null };
        const left = dfs(node.left);
        const right = dfs(node.right);
        if (left.depth > right.depth) return { depth: left.depth + 1, node: left.node };
        if (right.depth > left.depth) return { depth: right.depth + 1, node: right.node };
        return { depth: left.depth + 1, node: node };
    };
    return dfs(root).node;
};
