// LeetCode 0549 - Binary Tree Longest Consecutive Sequence II
// https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/

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

    public int LongestConsecutive(TreeNode root) {
        Dfs(root);
        return best;
    }

    private (int inc, int dec) Dfs(TreeNode node) {
        if (node == null) {
            return (0, 0);
        }

        (int leftInc, int leftDec) = Dfs(node.left);
        (int rightInc, int rightDec) = Dfs(node.right);

        int inc = 1;
        int dec = 1;

        if (node.left != null) {
            if (node.left.val == node.val + 1) {
                inc = System.Math.Max(inc, leftInc + 1);
            } else if (node.left.val == node.val - 1) {
                dec = System.Math.Max(dec, leftDec + 1);
            }
        }
        if (node.right != null) {
            if (node.right.val == node.val + 1) {
                inc = System.Math.Max(inc, rightInc + 1);
            } else if (node.right.val == node.val - 1) {
                dec = System.Math.Max(dec, rightDec + 1);
            }
        }

        if (node.left != null && node.right != null) {
            if (node.left.val + 1 == node.val && node.val == node.right.val - 1) {
                best = System.Math.Max(best, leftDec + 1 + rightInc);
            }
            if (node.left.val - 1 == node.val && node.val == node.right.val + 1) {
                best = System.Math.Max(best, leftInc + 1 + rightDec);
            }
        }

        best = System.Math.Max(best, System.Math.Max(inc, dec));
        return (inc, dec);
    }
}
