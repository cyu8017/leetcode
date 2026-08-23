// LeetCode 3831 - Median Of A Binary Search Tree Level
// https://leetcode.com/problems/median_of_a_binary_search_tree_level/

import java.util.ArrayList;
import java.util.List;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    private List<Integer> nums;

    public int levelMedian(TreeNode root, int level) {
        nums = new ArrayList<>();
        dfs(root, 0, level);
        if (nums.isEmpty()) return -1;
        return nums.get(nums.size() / 2);
    }

    private void dfs(TreeNode node, int i, int level) {
        if (node == null) return;
        dfs(node.left, i + 1, level);
        if (i == level) nums.add(node.val);
        dfs(node.right, i + 1, level);
    }
}
