// LeetCode 0094 - Binary Tree Inorder Traversal
// https://leetcode.com/problems/binary-tree-inorder-traversal/

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
    public IList<int> InorderTraversal(TreeNode root) {
        var result = new List<int>();
        var stack = new Stack<TreeNode>();
        var current = root;
        while (current != null || stack.Count > 0) {
            while (current != null) {
                stack.Push(current);
                current = current.left;
            }
            current = stack.Pop();
            result.Add(current.val);
            current = current.right;
        }
        return result;
    }
}
