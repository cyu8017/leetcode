// LeetCode 0872 - Leaf-Similar Trees
// https://leetcode.com/problems/leaf-similar-trees/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {boolean}
 */
var leafSimilar = function(root1, root2) {
    const leaves = (node) => {
        const result = [];
        const dfs = (cur) => {
            if (!cur) return;
            if (!cur.left && !cur.right) {
                result.push(cur.val);
                return;
            }
            dfs(cur.left);
            dfs(cur.right);
        };
        dfs(node);
        return result;
    };
    const a = leaves(root1), b = leaves(root2);
    if (a.length !== b.length) return false;
    for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false;
    return true;
};
