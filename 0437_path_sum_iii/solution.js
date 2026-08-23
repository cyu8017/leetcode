// LeetCode 0437 - Path Sum III
// https://leetcode.com/problems/path-sum-iii/

class Solution {
    pathSum(root, targetSum) {
        const prefixCounts = new Map([[0, 1]]);

        const dfs = (node, current) => {
            if (!node) return 0;
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

module.exports = { Solution };
