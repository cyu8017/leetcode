// LeetCode 1008 - Construct Binary Search Tree from Preorder Traversal
// https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

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
    private int i;
    private int[] preorder;

    public TreeNode BstFromPreorder(int[] preorder) {
        this.preorder = preorder;
        i = 0;
        return Build(int.MaxValue);
    }

    private TreeNode Build(int bound) {
        if (i == preorder.Length || preorder[i] > bound) return null;
        var root = new TreeNode(preorder[i++]);
        root.left = Build(root.val);
        root.right = Build(bound);
        return root;
    }
}
