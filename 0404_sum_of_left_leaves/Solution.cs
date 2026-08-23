// LeetCode 0404 - Sum of Left Leaves

// https://leetcode.com/problems/sum-of-left-leaves/



public class TreeNode {

    public int val;

    public TreeNode left;

    public TreeNode right;

    public TreeNode() {}

    public TreeNode(int val) { this.val = val; }

    public TreeNode(int val, TreeNode left, TreeNode right) {

        this.val = val;

        this.left = left;

        this.right = right;

    }

}



public class Solution {

    public int SumOfLeftLeaves(TreeNode root) {

        if (root == null) {

            return 0;

        }



        int total = 0;



        if (root.left != null && root.left.left == null && root.left.right == null) {

            total += root.left.val;

        } else {

            total += SumOfLeftLeaves(root.left);

        }



        total += SumOfLeftLeaves(root.right);



        return total;

    }

}
