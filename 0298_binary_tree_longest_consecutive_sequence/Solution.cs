// LeetCode 0298 - Binary Tree Longest Consecutive Sequence
// https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/

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
    public int LongestConsecutive(TreeNode root) {
        return Dfs(root, null, 0);
    }

    private int Dfs(TreeNode node, TreeNode parent, int length) {
        if (node == null) {
            return 0;
        }
        int current = parent != null && parent.val + 1 == node.val ? length + 1 : 1;
        return Math.Max(current, Math.Max(Dfs(node.left, node, current), Dfs(node.right, node, current)));
    }
}
