// LeetCode 1110 - Delete Nodes And Return Forest
// https://leetcode.com/problems/delete-nodes-and-return-forest/

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
 * @param {number[]} to_delete
 * @return {TreeNode[]}
 */
var delNodes = function(root, to_delete) {
    const deleteSet = new Set(to_delete);
    const forest = [];
    const dfs = (node, isRoot) => {
        if (!node) return null;
        const removed = deleteSet.has(node.val);
        if (isRoot && !removed) forest.push(node);
        node.left = dfs(node.left, removed);
        node.right = dfs(node.right, removed);
        return removed ? null : node;
    };
    dfs(root, true);
    return forest;
};
