// LeetCode 2196 - Create Binary Tree From Descriptions
// https://leetcode.com/problems/create-binary-tree-from-descriptions/

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
    public TreeNode CreateBinaryTree(int[][] descriptions) {
        var nodes = new Dictionary<int, TreeNode>();
        var child = new HashSet<int>();
        foreach (var d in descriptions) {
            int p = d[0], c = d[1], isLeft = d[2];
            if (!nodes.ContainsKey(p)) nodes[p] = new TreeNode(p);
            if (!nodes.ContainsKey(c)) nodes[c] = new TreeNode(c);
            if (isLeft == 1) nodes[p].left = nodes[c];
            else nodes[p].right = nodes[c];
            child.Add(c);
        }
        foreach (var kv in nodes)
            if (!child.Contains(kv.Key)) return kv.Value;
        return null;
    }
}
