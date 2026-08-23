// LeetCode 3831 - Median Of A Binary Search Tree Level
// https://leetcode.com/problems/median-of-a-binary-search-tree-level/

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
    public int LevelMedian(TreeNode root, int level) {
        var nums = new List<int>();
        void Dfs(TreeNode node, int i) {
            if (node == null) return;
            Dfs(node.left, i + 1);
            if (i == level) nums.Add(node.val);
            Dfs(node.right, i + 1);
        }
        Dfs(root, 0);
        if (nums.Count == 0) return -1;
        return nums[nums.Count / 2];
    }
}
