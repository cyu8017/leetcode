// LeetCode 1586 - Binary Search Tree Iterator II
// https://leetcode.com/problems/binary-search-tree-iterator-ii/

using System.Collections.Generic;

public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val; this.left = left; this.right = right;
    }
}

public class BSTIterator {
    private readonly List<int> values = new List<int>();
    private int index = -1;

    public BSTIterator(TreeNode root) {
        var stack = new Stack<TreeNode>();
        while (stack.Count > 0 || root != null) {
            while (root != null) {
                stack.Push(root);
                root = root.left;
            }
            root = stack.Pop();
            values.Add(root.val);
            root = root.right;
        }
    }

    public bool HasNext() => index + 1 < values.Count;
    public int Next() => values[++index];
    public bool HasPrev() => index > 0;
    public int Prev() => values[--index];
}
