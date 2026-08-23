// LeetCode 0559 - Maximum Depth of N-ary Tree
// https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

/**
 * // Definition for a Node.
 * function Node(val,children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/**
 * @param {Node|null} root
 * @return {number}
 */
var maxDepth = function(root) {
    if (root == null) return 0;
    if (!root.children || root.children.length === 0) return 1;
    let best = 0;
    for (const child of root.children) best = Math.max(best, maxDepth(child));
    return best + 1;
};
