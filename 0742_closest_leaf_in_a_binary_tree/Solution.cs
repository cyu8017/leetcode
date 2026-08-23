// LeetCode 0742 - Closest Leaf in a Binary Tree
// https://leetcode.com/problems/closest-leaf-in-a-binary-tree/

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
    public int FindClosestLeaf(TreeNode root, int k) {
        var graph = new Dictionary<int, List<int>>();
        var leaves = new HashSet<int>();
        Build(root, null, graph, leaves);
        var q = new Queue<int>();
        var seen = new HashSet<int> { k };
        q.Enqueue(k);
        while (q.Count > 0) {
            int value = q.Dequeue();
            if (leaves.Contains(value)) return value;
            if (!graph.ContainsKey(value)) continue;
            foreach (int neighbor in graph[value]) {
                if (seen.Add(neighbor)) q.Enqueue(neighbor);
            }
        }
        return -1;
    }

    private void Build(TreeNode node, TreeNode parent, Dictionary<int, List<int>> graph, HashSet<int> leaves) {
        if (node == null) return;
        if (!graph.ContainsKey(node.val)) graph[node.val] = new List<int>();
        if (parent != null) {
            if (!graph.ContainsKey(parent.val)) graph[parent.val] = new List<int>();
            graph[node.val].Add(parent.val);
            graph[parent.val].Add(node.val);
        }
        if (node.left == null && node.right == null) leaves.Add(node.val);
        Build(node.right, node, graph, leaves);
        Build(node.left, node, graph, leaves);
    }
}
