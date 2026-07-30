// LeetCode 1214 - Two Sum BSTs
// https://leetcode.com/problems/two-sum-bsts/

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
    public bool TwoSumBSTs(TreeNode root1, TreeNode root2, int target) {
        var values = new HashSet<int>();
        var stack = new Stack<TreeNode>();
        if (root1 != null) stack.Push(root1);
        while (stack.Count > 0) {
            var node = stack.Pop();
            values.Add(node.val);
            if (node.left != null) stack.Push(node.left);
            if (node.right != null) stack.Push(node.right);
        }

        stack.Clear();
        if (root2 != null) stack.Push(root2);
        while (stack.Count > 0) {
            var node = stack.Pop();
            if (values.Contains(target - node.val)) return true;
            if (node.left != null) stack.Push(node.left);
            if (node.right != null) stack.Push(node.right);
        }
        return false;
    }
}
