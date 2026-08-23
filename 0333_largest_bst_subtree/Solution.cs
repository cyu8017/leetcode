// LeetCode 0333 - Largest BST Subtree

// https://leetcode.com/problems/largest-bst-subtree/



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

    private int best = 0;



    public int LargestBSTSubtree(TreeNode root) {

        Dfs(root);

        return best;

    }



    private int[] Dfs(TreeNode node) {

        if (node == null) {

            return new int[] {1, int.MaxValue, int.MinValue, 0};

        }



        int[] left = Dfs(node.left);

        int[] right = Dfs(node.right);



        if (left[0] == 1 && right[0] == 1 && left[2] < node.val && right[1] > node.val) {

            int size = left[3] + right[3] + 1;

            best = Math.Max(best, size);

            return new int[] {1, Math.Min(left[1], node.val), Math.Max(right[2], node.val), size};

        }



        return new int[] {0, 0, 0, 0};

    }

}
