// LeetCode 0333 - Largest BST Subtree

// https://leetcode.com/problems/largest-bst-subtree/



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

    private int best = 0;



    public int largestBSTSubtree(TreeNode root) {

        dfs(root);

        return best;

    }



    private int[] dfs(TreeNode node) {

        if (node == null) {

            return new int[] {1, Integer.MAX_VALUE, Integer.MIN_VALUE, 0};

        }



        int[] left = dfs(node.left);

        int[] right = dfs(node.right);



        if (left[0] == 1 && right[0] == 1 && left[2] < node.val && right[1] > node.val) {

            int size = left[3] + right[3] + 1;

            best = Math.max(best, size);

            return new int[] {1, Math.min(left[1], node.val), Math.max(right[2], node.val), size};

        }



        return new int[] {0, 0, 0, 0};

    }

}
