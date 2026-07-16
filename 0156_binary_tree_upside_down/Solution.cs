public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) { this.val = val; this.left = left; this.right = right; }
}

public class Solution {
    public TreeNode UpsideDownBinaryTree(TreeNode root) {
        TreeNode previous = null, previousRight = null, current = root;
        while (current != null) {
            TreeNode next = current.left;
            current.left = previousRight;
            previousRight = current.right;
            current.right = previous;
            previous = current;
            current = next;
        }
        return previous;
    }
}