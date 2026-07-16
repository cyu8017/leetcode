// LeetCode 0095 - Unique Binary Search Trees II
// https://leetcode.com/problems/unique-binary-search-trees-ii/

import java.util.*;

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
    public List<TreeNode> generateTrees(int n) {
        if (n == 0) {
            return new ArrayList<>();
        }
        return build(1, n);
    }

    private List<TreeNode> build(int start, int end) {
        List<TreeNode> trees = new ArrayList<>();
        if (start > end) {
            trees.add(null);
            return trees;
        }
        for (int rootVal = start; rootVal <= end; rootVal++) {
            List<TreeNode> leftTrees = build(start, rootVal - 1);
            List<TreeNode> rightTrees = build(rootVal + 1, end);
            for (TreeNode left : leftTrees) {
                for (TreeNode right : rightTrees) {
                    trees.add(new TreeNode(rootVal, left, right));
                }
            }
        }
        return trees;
    }
}
