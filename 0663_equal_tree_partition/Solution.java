// LeetCode 0663 - Equal Tree Partition
// https://leetcode.com/problems/equal-tree-partition/

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
    private final List<Integer> subtreeSums = new ArrayList<>();

    public boolean checkEqualTree(TreeNode root) {
        subtreeSums.clear();
        int total = dfs(root);
        if (!subtreeSums.isEmpty()) {
            subtreeSums.remove(subtreeSums.size() - 1);
        }
        if (total % 2 != 0) {
            return false;
        }
        int half = total / 2;
        for (int sum : subtreeSums) {
            if (sum == half) {
                return true;
            }
        }
        return false;
    }

    private int dfs(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int total = node.val + dfs(node.left) + dfs(node.right);
        subtreeSums.add(total);
        return total;
    }
}
