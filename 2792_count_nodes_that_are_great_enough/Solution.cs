// LeetCode 2792 - Count Nodes That Are Great Enough
// https://leetcode.com/problems/count-nodes-that-are-great-enough/

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
    public int CountGreatEnoughNodes(TreeNode root, int k) {
        int ans = 0;
        List<int> Dfs(TreeNode node) {
            if (node == null) return new List<int>();
            var vals = new List<int> { node.val };
            vals.AddRange(Dfs(node.left));
            vals.AddRange(Dfs(node.right));
            int smaller = 0;
            foreach (int v in vals) if (v < node.val) smaller++;
            if (smaller >= k) ans++;
            return vals;
        }
        Dfs(root);
        return ans;
    }
}
