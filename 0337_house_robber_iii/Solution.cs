// LeetCode 0337 - House Robber III

// https://leetcode.com/problems/house-robber-iii/



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

    public int Rob(TreeNode root) {

        int[] result = Dfs(root);

        return Math.Max(result[0], result[1]);

    }



    private int[] Dfs(TreeNode node) {

        if (node == null) {

            return new int[] {0, 0};

        }



        int[] left = Dfs(node.left);

        int[] right = Dfs(node.right);



        int withRob = node.val + left[1] + right[1];

        int withoutRob = Math.Max(left[0], left[1]) + Math.Max(right[0], right[1]);

        return new int[] {withRob, withoutRob};

    }

}
