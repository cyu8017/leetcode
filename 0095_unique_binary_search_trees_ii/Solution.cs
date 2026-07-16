// LeetCode 0095 - Unique Binary Search Trees II
// https://leetcode.com/problems/unique-binary-search-trees-ii/

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
    public IList<TreeNode> GenerateTrees(int n) {
        if (n == 0) {
            return new List<TreeNode>();
        }
        return Build(1, n);
    }

    private IList<TreeNode> Build(int start, int end) {
        var trees = new List<TreeNode>();
        if (start > end) {
            trees.Add(null);
            return trees;
        }
        for (int rootVal = start; rootVal <= end; rootVal++) {
            var leftTrees = Build(start, rootVal - 1);
            var rightTrees = Build(rootVal + 1, end);
            foreach (var left in leftTrees) {
                foreach (var right in rightTrees) {
                    trees.Add(new TreeNode(rootVal, left, right));
                }
            }
        }
        return trees;
    }
}
