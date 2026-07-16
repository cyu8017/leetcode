"use strict";
// LeetCode 0437 - Path Sum III
// https://leetcode.com/problems/path-sum-iii/
Object.defineProperty(exports, "__esModule", { value: true });
exports.Solution = exports.TreeNode = void 0;
class TreeNode {
    constructor(val = 0, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
exports.TreeNode = TreeNode;
class Solution {
    pathSum(root, targetSum) {
        const prefixCounts = new Map([[0, 1]]);
        const dfs = (node, current) => {
            if (!node)
                return 0;
            current += node.val;
            let total = prefixCounts.get(current - targetSum) ?? 0;
            prefixCounts.set(current, (prefixCounts.get(current) ?? 0) + 1);
            total += dfs(node.left, current);
            total += dfs(node.right, current);
            prefixCounts.set(current, prefixCounts.get(current) - 1);
            return total;
        };
        return dfs(root, 0);
    }
}
exports.Solution = Solution;
