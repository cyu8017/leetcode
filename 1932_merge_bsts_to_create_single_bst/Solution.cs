// LeetCode 1932 - Merge BSTs to Create Single BST
// https://leetcode.com/problems/merge-bsts-to-create-single-bst/

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
    public TreeNode CanMerge(IList<TreeNode> trees) {
        var valueToRoot = new Dictionary<int, TreeNode>();
        var count = new Dictionary<int, int>();
        foreach (var tree in trees) {
            valueToRoot[tree.val] = tree;
            count[tree.val] = count.GetValueOrDefault(tree.val) + 1;
            if (tree.left != null) count[tree.left.val] = count.GetValueOrDefault(tree.left.val) + 1;
            if (tree.right != null) count[tree.right.val] = count.GetValueOrDefault(tree.right.val) + 1;
        }
        TreeNode root = null;
        int roots = 0;
        foreach (var t in trees) {
            if (count[t.val] == 1) { root = t; roots++; }
        }
        if (roots != 1) return null;
        valueToRoot.Remove(root.val);
        if (!Merge(root, valueToRoot) || valueToRoot.Count > 0) return null;
        return IsValidBst(root, long.MinValue, long.MaxValue) ? root : null;
    }

    bool Merge(TreeNode node, Dictionary<int, TreeNode> valueToRoot) {
        if (node == null) return true;
        if (node.left != null && valueToRoot.ContainsKey(node.left.val)) {
            node.left = valueToRoot[node.left.val];
            valueToRoot.Remove(node.left.val);
        }
        if (node.right != null && valueToRoot.ContainsKey(node.right.val)) {
            node.right = valueToRoot[node.right.val];
            valueToRoot.Remove(node.right.val);
        }
        return Merge(node.left, valueToRoot) && Merge(node.right, valueToRoot);
    }

    bool IsValidBst(TreeNode node, long lo, long hi) {
        if (node == null) return true;
        if (!(lo < node.val && node.val < hi)) return false;
        return IsValidBst(node.left, lo, node.val) && IsValidBst(node.right, node.val, hi);
    }
}