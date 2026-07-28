// LeetCode 1028 - Recover a Tree From Preorder Traversal
// https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

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
    public TreeNode RecoverFromPreorder(string traversal) {
        var stack = new List<TreeNode>();
        int i = 0, n = traversal.Length;
        while (i < n) {
            int depth = 0;
            while (i < n && traversal[i] == '-') { depth++; i++; }
            int start = i;
            while (i < n && char.IsDigit(traversal[i])) i++;
            var node = new TreeNode(int.Parse(traversal.Substring(start, i - start)));
            while (stack.Count > depth) stack.RemoveAt(stack.Count - 1);
            if (stack.Count > 0) {
                if (stack[stack.Count - 1].left == null) stack[stack.Count - 1].left = node;
                else stack[stack.Count - 1].right = node;
            }
            stack.Add(node);
        }
        return stack[0];
    }
}
