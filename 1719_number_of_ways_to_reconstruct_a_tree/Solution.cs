// LeetCode 1719 - Number Of Ways To Reconstruct A Tree
// https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/

public class Solution {
    public int CheckWays(int[][] pairs) {
        var graph = new Dictionary<int, HashSet<int>>();
        foreach (var pair in pairs) {
            int a = pair[0];
            int b = pair[1];
            if (!graph.ContainsKey(a)) {
                graph[a] = new HashSet<int>();
            }
            if (!graph.ContainsKey(b)) {
                graph[b] = new HashSet<int>();
            }
            graph[a].Add(b);
            graph[b].Add(a);
        }
        int n = graph.Count;
        int root = -1;
        foreach (var entry in graph) {
            if (entry.Value.Count == n - 1) {
                root = entry.Key;
                break;
            }
        }
        if (root == -1) {
            return 0;
        }
        int ans = 1;
        foreach (var entry in graph) {
            int node = entry.Key;
            var neighbors = entry.Value;
            if (node == root) {
                continue;
            }
            int parent = -1;
            int parentDegree = n + 1;
            foreach (int nei in neighbors) {
                int neiDegree = graph[nei].Count;
                if (neiDegree >= neighbors.Count && neiDegree < parentDegree) {
                    parent = nei;
                    parentDegree = neiDegree;
                }
            }
            if (parent == -1) {
                return 0;
            }
            foreach (int nei in neighbors) {
                if (nei != parent && !graph[parent].Contains(nei)) {
                    return 0;
                }
            }
            if (graph[parent].Count == neighbors.Count) {
                ans = 2;
            }
        }
        return ans;
    }
}
