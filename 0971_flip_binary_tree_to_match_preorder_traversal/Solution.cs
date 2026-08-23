// LeetCode 0971 - Flip Binary Tree To Match Preorder Traversal
// https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/

using System.Collections.Generic;

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
    public IList<int> FlipMatchVoyage(TreeNode root, int[] voyage) {
        int i = 0;
        var ans = new List<int>();
        bool Dfs(TreeNode node) {
            if (node == null) return true;
            if (node.val != voyage[i]) return false;
            i++;
            if (node.left != null && node.left.val != voyage[i]) {
                ans.Add(node.val);
                return Dfs(node.right) && Dfs(node.left);
            }
            return Dfs(node.left) && Dfs(node.right);
        }
        return Dfs(root) ? ans : new List<int> { -1 };
    }
}
