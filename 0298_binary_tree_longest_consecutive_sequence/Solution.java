// LeetCode 0298 - Binary Tree Longest Consecutive Sequence
// https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/

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
    public int longestConsecutive(TreeNode root) {
        return dfs(root, null, 0);
    }

    private int dfs(TreeNode node, TreeNode parent, int length) {
        if (node == null) {
            return 0;
        }
        int current = parent != null && parent.val + 1 == node.val ? length + 1 : 1;
        return Math.max(current, Math.max(dfs(node.left, node, current), dfs(node.right, node, current)));
    }
}
