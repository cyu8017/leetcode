// LeetCode 2458 - Height of Binary Tree After Subtree Removal Queries
// https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/

using System;
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
    private Dictionary<int, int> height = new Dictionary<int, int>();
    private Dictionary<int, int> level = new Dictionary<int, int>();
    private Dictionary<int, List<int>> levelMax = new Dictionary<int, List<int>>();

    public int[] TreeQueries(TreeNode root, int[] queries) {
        Dfs(root, 0);
        int[] ans = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            int q = queries[i];
            int d = level[q], h = height[q];
            var top = levelMax[d];
            if (top[0] == h) {
                if (top.Count > 1) ans[i] = d + top[1];
                else ans[i] = d - 1;
            } else {
                ans[i] = d + top[0];
            }
        }
        return ans;
    }

    private int Dfs(TreeNode node, int d) {
        if (node == null) return -1;
        level[node.val] = d;
        int h = 1 + Math.Max(Dfs(node.left, d + 1), Dfs(node.right, d + 1));
        height[node.val] = h;
        if (!levelMax.ContainsKey(d)) levelMax[d] = new List<int>();
        var arr = levelMax[d];
        if (arr.Count == 0) arr.Add(h);
        else if (h >= arr[0]) {
            if (arr.Count == 1) arr.Add(arr[0]);
            else arr[1] = arr[0];
            arr[0] = h;
        } else if (arr.Count == 1 || h > arr[1]) {
            if (arr.Count == 1) arr.Add(h);
            else arr[1] = h;
        }
        return h;
    }
}
