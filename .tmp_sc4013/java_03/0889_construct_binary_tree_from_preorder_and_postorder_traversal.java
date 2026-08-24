// LeetCode 0889 - Construct Binary Tree from Preorder and Postorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

import java.util.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    private Map<Integer, Integer> postIndex;
    private int[] preorder;

    public TreeNode constructFromPrePost(int[] preorder, int[] postorder) {
        this.preorder = preorder;
        postIndex = new HashMap<>();
        for (int i = 0; i < postorder.length; i++) postIndex.put(postorder[i], i);
        int n = preorder.length;
        return build(0, n - 1, 0, n - 1);
    }

    private TreeNode build(int preLo, int preHi, int postLo, int postHi) {
        if (preLo > preHi) return null;
        TreeNode root = new TreeNode(preorder[preLo]);
        if (preLo == preHi) return root;
        int leftVal = preorder[preLo + 1];
        int leftPost = postIndex.get(leftVal);
        int leftSize = leftPost - postLo + 1;
        root.left = build(preLo + 1, preLo + leftSize, postLo, leftPost);
        root.right = build(preLo + leftSize + 1, preHi, leftPost + 1, postHi - 1);
        return root;
    }
}
