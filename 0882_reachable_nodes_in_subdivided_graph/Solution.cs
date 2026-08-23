// LeetCode 0882 - Reachable Nodes In Subdivided Graph
// https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/

using System;
using System.Collections.Generic;

public class Solution {
    public int ReachableNodes(int[][] edges, int maxMoves, int n) {
        var graph = new Dictionary<int, int>[n];
        for (int i = 0; i < n; i++) graph[i] = new Dictionary<int, int>();
        foreach (var e in edges) {
            graph[e[0]][e[1]] = e[2];
            graph[e[1]][e[0]] = e[2];
        }
        var pq = new PriorityQueue<int, int>();
        pq.Enqueue(0, -maxMoves);
        var seen = new Dictionary<int, int>();
        while (pq.Count > 0) {
            pq.TryDequeue(out int node, out int negMoves);
            int moves = -negMoves;
            if (seen.ContainsKey(node)) continue;
            seen[node] = moves;
            foreach (var kv in graph[node]) {
                int remain = moves - kv.Value - 1;
                if (!seen.ContainsKey(kv.Key) && remain >= 0) pq.Enqueue(kv.Key, -remain);
            }
        }
        int ans = seen.Count;
        foreach (var e in edges) {
            int left = seen.ContainsKey(e[0]) ? seen[e[0]] : 0;
            int right = seen.ContainsKey(e[1]) ? seen[e[1]] : 0;
            ans += Math.Min(e[2], left + right);
        }
        return ans;
    }
}
