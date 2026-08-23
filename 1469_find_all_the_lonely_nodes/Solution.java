// LeetCode 1469 - Find All The Lonely Nodes
// https://leetcode.com/problems/find-all-the-lonely-nodes/

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
    public List<Integer> getLonelyNodes(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        dfs(root, ans);
        return ans;
    }

    private void dfs(TreeNode node, List<Integer> ans) {
        if (node == null) return;
        if ((node.left == null) != (node.right == null)) {
            ans.add(node.left != null ? node.left.val : node.right.val);
        }
        dfs(node.left, ans);
        dfs(node.right, ans);
    }
}
