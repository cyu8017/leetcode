// LeetCode 0589 - N-ary Tree Preorder Traversal
// https://leetcode.com/problems/n-ary-tree-preorder-traversal/

/**
 * // Definition for a Node.
 * function Node(val, children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/**
 * @param {Node|null} root
 * @return {number[]}
 */
var preorder = function(root) {
    const result = [];
    const dfs = (node) => {
        if (node == null) return;
        result.push(node.val);
        if (node.children) for (const child of node.children) dfs(child);
    };
    dfs(root);
    return result;
};
