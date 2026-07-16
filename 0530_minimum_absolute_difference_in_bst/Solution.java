// LeetCode 0530 - Minimum Absolute Difference in BST
// https://leetcode.com/problems/minimum-absolute-difference-in-bst/

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {}

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public int getMinimumDifference(TreeNode root) {
        int[] state = new int[] {Integer.MAX_VALUE};
        Integer[] previous = new Integer[1];
        inorder(root, previous, state);
        return state[0];
    }

    private void inorder(TreeNode node, Integer[] previous, int[] best) {
        if (node == null) {
            return;
        }
        inorder(node.left, previous, best);
        if (previous[0] != null) {
            best[0] = Math.min(best[0], node.val - previous[0]);
        }
        previous[0] = node.val;
        inorder(node.right, previous, best);
    }
}
