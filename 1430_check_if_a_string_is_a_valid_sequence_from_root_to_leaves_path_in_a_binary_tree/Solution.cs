// LeetCode 1430 - Check If A String Is A Valid Sequence From Root To Leaves Path In A Binary Tree
// https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/

public class TreeNode {
    public int val; public TreeNode left; public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val; this.left = left; this.right = right;
    }
}
public class Solution {
    public bool IsValidSequence(TreeNode root, int[] arr) {
        bool Visit(TreeNode node, int index) {
            if (node == null || index == arr.Length || node.val != arr[index]) return false;
            if (node.left == null && node.right == null) return index == arr.Length - 1;
            return Visit(node.left, index + 1) || Visit(node.right, index + 1);
        }
        return Visit(root, 0);
    }
}
