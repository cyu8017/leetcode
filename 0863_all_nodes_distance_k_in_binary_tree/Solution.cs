// LeetCode 0863 - All Nodes Distance K in Binary Tree
// https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

using System.Collections.Generic;

public class Solution {
    public IList<int> DistanceK(TreeNode root, TreeNode target, int k) {
        var graph = new Dictionary<TreeNode, List<TreeNode>>();
        void Build(TreeNode node, TreeNode parent) {
            if (node == null) return;
            if (!graph.ContainsKey(node)) graph[node] = new List<TreeNode>();
            if (parent != null) {
                graph[node].Add(parent);
                if (!graph.ContainsKey(parent)) graph[parent] = new List<TreeNode>();
                graph[parent].Add(node);
            }
            Build(node.left, node);
            Build(node.right, node);
        }
        Build(root, null);
        var queue = new Queue<(TreeNode node, int dist)>();
        queue.Enqueue((target, 0));
        var seen = new HashSet<TreeNode> { target };
        var ans = new List<int>();
        while (queue.Count > 0) {
            var (node, dist) = queue.Dequeue();
            if (dist == k) { ans.Add(node.val); continue; }
            if (!graph.ContainsKey(node)) continue;
            foreach (var nei in graph[node]) {
                if (seen.Add(nei)) queue.Enqueue((nei, dist + 1));
            }
        }
        return ans;
    }
}
