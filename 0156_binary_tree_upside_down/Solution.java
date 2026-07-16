class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) { this.val = val; this.left = left; this.right = right; }
}

class Solution {
    public TreeNode upsideDownBinaryTree(TreeNode root) {
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