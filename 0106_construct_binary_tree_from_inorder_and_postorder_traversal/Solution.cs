// LeetCode 0106 - Construct Binary Tree from Inorder and Postorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

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
    private int postIndex;
    private int[] postorder;
    private Dictionary<int, int> index;

    public TreeNode BuildTree(int[] inorder, int[] postorder) {
        this.postorder = postorder;
        this.postIndex = postorder.Length - 1;
        this.index = new Dictionary<int, int>();
        for (int i = 0; i < inorder.Length; i++) {
            index[inorder[i]] = i;
        }
        return Build(0, inorder.Length - 1);
    }

    private TreeNode Build(int left, int right) {
        if (left > right) {
            return null;
        }
        int rootVal = postorder[postIndex--];
        int mid = index[rootVal];
        TreeNode root = new TreeNode(rootVal);
        root.right = Build(mid + 1, right);
        root.left = Build(left, mid - 1);
        return root;
    }
}