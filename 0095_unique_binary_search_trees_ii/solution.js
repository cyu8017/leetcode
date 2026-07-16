// LeetCode 0095 - Unique Binary Search Trees II
// https://leetcode.com/problems/unique-binary-search-trees-ii/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val);
    this.left = (left===undefined ? null : left);
    this.right = (right===undefined ? null : right);
}

/**
 * @param {number} n
 * @return {TreeNode[]}
 */
var generateTrees = function(n) {
    function build(start, end) {
        if (start > end) {
            return [null];
        }
        var trees = [];
        for (var rootVal = start; rootVal <= end; rootVal++) {
            var leftTrees = build(start, rootVal - 1);
            var rightTrees = build(rootVal + 1, end);
            for (var i = 0; i < leftTrees.length; i++) {
                for (var j = 0; j < rightTrees.length; j++) {
                    trees.push(new TreeNode(rootVal, leftTrees[i], rightTrees[j]));
                }
            }
        }
        return trees;
    }
    return n ? build(1, n) : [];
};
