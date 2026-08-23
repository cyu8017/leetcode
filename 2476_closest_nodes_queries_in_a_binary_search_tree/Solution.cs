// LeetCode 2476 - Closest Nodes Queries in a Binary Search Tree
// https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/

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
    public IList<IList<int>> ClosestNodes(TreeNode root, IList<int> queries) {
        var vals = new List<int>();
        void Inorder(TreeNode node) {
            if (node == null) return;
            Inorder(node.left);
            vals.Add(node.val);
            Inorder(node.right);
        }
        Inorder(root);
        var ans = new List<IList<int>>();
        foreach (int q in queries) {
            int j = LowerBound(vals, q);
            int mx = j < vals.Count ? vals[j] : -1;
            int mn = -1;
            if (j < vals.Count && vals[j] == q) mn = q;
            else if (j > 0) mn = vals[j - 1];
            ans.Add(new List<int> { mn, mx });
        }
        return ans;
    }

    private int LowerBound(List<int> vals, int q) {
        int lo = 0, hi = vals.Count;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (vals[mid] < q) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
