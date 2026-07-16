// LeetCode 0105 - Construct Binary Tree from Preorder and Inorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

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
    private int preIndex;
    private int[] preorder;
    private Dictionary<int, int> index;

    public TreeNode BuildTree(int[] preorder, int[] inorder) {
        this.preorder = preorder;
        this.preIndex = 0;
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
        int rootVal = preorder[preIndex++];
        int mid = index[rootVal];
        TreeNode root = new TreeNode(rootVal);
        root.left = Build(left, mid - 1);
        root.right = Build(mid + 1, right);
        return root;
    }
}