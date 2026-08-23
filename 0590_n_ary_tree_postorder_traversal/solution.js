// LeetCode 0590 - N-ary Tree Postorder Traversal
// https://leetcode.com/problems/n-ary-tree-postorder-traversal/

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
var postorder = function(root) {
    const result = [];
    const dfs = (node) => {
        if (node == null) return;
        if (node.children) for (const child of node.children) dfs(child);
        result.push(node.val);
    };
    dfs(root);
    return result;
};
