// LeetCode 1379 - Find A Corresponding Node Of A Binary Tree In A Clone Of That Tree
// https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

public class TreeNode {
    public int val; public TreeNode left; public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val; this.left = left; this.right = right;
    }
}
public class Solution {
    public TreeNode GetTargetCopy(TreeNode original, TreeNode cloned, TreeNode target) {
        var stack = new System.Collections.Generic.Stack<(TreeNode, TreeNode)>();
        stack.Push((original, cloned));
        while (stack.Count > 0) {
            var (a, b) = stack.Pop();
            if (a == target || a.val == target.val) return b;
            if (a.left != null) stack.Push((a.left, b.left));
            if (a.right != null) stack.Push((a.right, b.right));
        }
        return null;
    }
}
