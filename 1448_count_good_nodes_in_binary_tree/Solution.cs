// LeetCode 1448 - Count Good Nodes In Binary Tree
// https://leetcode.com/problems/count-good-nodes-in-binary-tree/

public class TreeNode {
    public int val; public TreeNode left; public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val; this.left = left; this.right = right;
    }
}
public class Solution {
    public int GoodNodes(TreeNode root) {
        int Visit(TreeNode node, int maximum) {
            if (node == null) return 0;
            int good = node.val >= maximum ? 1 : 0;
            maximum = System.Math.Max(maximum, node.val);
            return good + Visit(node.left, maximum) + Visit(node.right, maximum);
        }
        return Visit(root, int.MinValue);
    }
}
