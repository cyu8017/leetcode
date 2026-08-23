// LeetCode 0298 - Binary Tree Longest Consecutive Sequence
// https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/

/**
 * @param {TreeNode|null} root
 * @return {number}
 */
var longestConsecutive = function(root) {
    function dfs(node, parent, length) {
        if (!node) {
            return 0;
        }
        const current = parent && parent.val + 1 === node.val ? length + 1 : 1;
        return Math.max(current, dfs(node.left, node, current), dfs(node.right, node, current));
    }
    return dfs(root, null, 0);
};
