// LeetCode 0653 - Two Sum IV - Input is a BST
// https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

import java.util.HashSet;
import java.util.Set;

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
    private final Set<Integer> seen = new HashSet<>();
    private int k;

    public boolean findTarget(TreeNode root, int k) {
        seen.clear();
        this.k = k;
        return dfs(root);
    }

    private boolean dfs(TreeNode node) {
        if (node == null) {
            return false;
        }
        if (seen.contains(k - node.val)) {
            return true;
        }
        seen.add(node.val);
        return dfs(node.left) || dfs(node.right);
    }
}
