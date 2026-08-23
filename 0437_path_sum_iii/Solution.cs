// LeetCode 0437 - Path Sum III
// https://leetcode.com/problems/path-sum-iii/

using System.Collections.Generic;

public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Solution {
    public int PathSum(TreeNode root, int targetSum) {
        Dictionary<long, int> prefixCounts = new Dictionary<long, int> { [0L] = 1 };
        return Dfs(root, 0L, targetSum, prefixCounts);
    }

    private int Dfs(TreeNode node, long current, int targetSum, Dictionary<long, int> prefixCounts) {
        if (node == null) {
            return 0;
        }
        current += node.val;
        int total = prefixCounts.GetValueOrDefault(current - targetSum, 0);
        prefixCounts[current] = prefixCounts.GetValueOrDefault(current, 0) + 1;
        total += Dfs(node.left, current, targetSum, prefixCounts);
        total += Dfs(node.right, current, targetSum, prefixCounts);
        prefixCounts[current]--;
        return total;
    }
}
