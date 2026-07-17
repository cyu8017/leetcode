// LeetCode 1740 - Find Distance in a Binary Tree
// https://leetcode.com/problems/find-distance-in-a-binary-tree/

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
    public int FindDistance(TreeNode root, int p, int q) {
        var graph = new Dictionary<int, List<int>>();
        Dfs(root, null, graph);
        var queue = new Queue<(int Node, int Dist)>();
        queue.Enqueue((p, 0));
        var seen = new HashSet<int> { p };
        while (queue.Count > 0) {
            var (node, dist) = queue.Dequeue();
            if (node == q) {
                return dist;
            }
            foreach (int nei in graph[node]) {
                if (seen.Add(nei)) {
                    queue.Enqueue((nei, dist + 1));
                }
            }
        }
        return -1;
    }

    private void Dfs(TreeNode node, TreeNode parent, Dictionary<int, List<int>> graph) {
        if (node == null) {
            return;
        }
        if (!graph.ContainsKey(node.val)) {
            graph[node.val] = new List<int>();
        }
        if (parent != null) {
            graph[node.val].Add(parent.val);
            graph[parent.val].Add(node.val);
        }
        Dfs(node.left, node, graph);
        Dfs(node.right, node, graph);
    }
}
