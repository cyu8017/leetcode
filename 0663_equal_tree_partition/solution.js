// LeetCode 0663 - Equal Tree Partition
// https://leetcode.com/problems/equal-tree-partition/

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
 * @return {boolean}
 */
var checkEqualTree = function(root) {
    const subtreeSums = [];
    const dfs = (node) => {
        if (node == null) return 0;
        const total = node.val + dfs(node.left) + dfs(node.right);
        subtreeSums.push(total);
        return total;
    };
    const total = dfs(root);
    if (subtreeSums.length) subtreeSums.pop();
    if (total % 2 !== 0) return false;
    const half = total / 2;
    return subtreeSums.includes(half);
};
