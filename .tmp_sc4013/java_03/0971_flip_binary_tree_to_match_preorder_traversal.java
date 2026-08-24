// LeetCode 0971 - Flip Binary Tree To Match Preorder Traversal
// https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/

import java.util.*;

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
    private int i = 0;
    private int[] voyage;
    private List<Integer> ans = new ArrayList<>();

    public List<Integer> flipMatchVoyage(TreeNode root, int[] voyage) {
        this.voyage = voyage;
        return dfs(root) ? ans : Arrays.asList(-1);
    }

    private boolean dfs(TreeNode node) {
        if (node == null) return true;
        if (node.val != voyage[i]) return false;
        i++;
        if (node.left != null && node.left.val != voyage[i]) {
            ans.add(node.val);
            return dfs(node.right) && dfs(node.left);
        }
        return dfs(node.left) && dfs(node.right);
    }
}
