// LeetCode 0437 - Path Sum III
// https://leetcode.com/problems/path-sum-iii/

import java.util.HashMap;
import java.util.Map;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {}

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public int pathSum(TreeNode root, int targetSum) {
        Map<Long, Integer> prefixCounts = new HashMap<>();
        prefixCounts.put(0L, 1);
        return dfs(root, 0L, targetSum, prefixCounts);
    }

    private int dfs(TreeNode node, long current, int targetSum, Map<Long, Integer> prefixCounts) {
        if (node == null) {
            return 0;
        }
        current += node.val;
        int total = prefixCounts.getOrDefault(current - targetSum, 0);
        prefixCounts.put(current, prefixCounts.getOrDefault(current, 0) + 1);
        total += dfs(node.left, current, targetSum, prefixCounts);
        total += dfs(node.right, current, targetSum, prefixCounts);
        prefixCounts.put(current, prefixCounts.get(current) - 1);
        return total;
    }
}
