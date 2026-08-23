// LeetCode 0889 - Construct Binary Tree from Preorder and Postorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

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
    public TreeNode ConstructFromPrePost(int[] preorder, int[] postorder) {
        var postIndex = new Dictionary<int, int>();
        for (int i = 0; i < postorder.Length; i++) postIndex[postorder[i]] = i;
        TreeNode Build(int preLo, int preHi, int postLo, int postHi) {
            if (preLo > preHi) return null;
            var root = new TreeNode(preorder[preLo]);
            if (preLo == preHi) return root;
            int leftVal = preorder[preLo + 1];
            int leftPost = postIndex[leftVal];
            int leftSize = leftPost - postLo + 1;
            root.left = Build(preLo + 1, preLo + leftSize, postLo, leftPost);
            root.right = Build(preLo + leftSize + 1, preHi, leftPost + 1, postHi - 1);
            return root;
        }
        int n = preorder.Length;
        return Build(0, n - 1, 0, n - 1);
    }
}
