// LeetCode 1469 - Find All The Lonely Nodes
// https://leetcode.com/problems/find-all-the-lonely-nodes/

using System.Collections.Generic;
public class TreeNode {
    public int val; public TreeNode left; public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val; this.left = left; this.right = right;
    }
}
public class Solution {
    public IList<int> GetLonelyNodes(TreeNode root) {
        var ans = new List<int>();
        void Dfs(TreeNode node) {
            if (node == null) return;
            if ((node.left == null) ^ (node.right == null))
                ans.Add((node.left ?? node.right).val);
            Dfs(node.left); Dfs(node.right);
        }
        Dfs(root); return ans;
    }
}
