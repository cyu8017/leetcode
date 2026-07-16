// LeetCode 0549 - Binary Tree Longest Consecutive Sequence II
// https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/

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
    private int best = 0;

    public int longestConsecutive(TreeNode root) {
        dfs(root);
        return best;
    }

    private int[] dfs(TreeNode node) {
        if (node == null) {
            return new int[] { 0, 0 };
        }

        int[] left = dfs(node.left);
        int[] right = dfs(node.right);
        int leftInc = left[0];
        int leftDec = left[1];
        int rightInc = right[0];
        int rightDec = right[1];

        int inc = 1;
        int dec = 1;

        if (node.left != null) {
            if (node.left.val == node.val + 1) {
                inc = Math.max(inc, leftInc + 1);
            } else if (node.left.val == node.val - 1) {
                dec = Math.max(dec, leftDec + 1);
            }
        }
        if (node.right != null) {
            if (node.right.val == node.val + 1) {
                inc = Math.max(inc, rightInc + 1);
            } else if (node.right.val == node.val - 1) {
                dec = Math.max(dec, rightDec + 1);
            }
        }

        if (node.left != null && node.right != null) {
            if (node.left.val + 1 == node.val && node.val == node.right.val - 1) {
                best = Math.max(best, leftDec + 1 + rightInc);
            }
            if (node.left.val - 1 == node.val && node.val == node.right.val + 1) {
                best = Math.max(best, leftInc + 1 + rightDec);
            }
        }

        best = Math.max(best, Math.max(inc, dec));
        return new int[] { inc, dec };
    }
}
