// LeetCode 0847 - Shortest Path Visiting All Nodes
// https://leetcode.com/problems/shortest-path-visiting-all-nodes/

using System.Collections.Generic;

public class Solution {
    public int ShortestPathLength(int[][] graph) {
        int n = graph.Length, target = (1 << n) - 1;
        var queue = new Queue<(int node, int mask, int dist)>();
        var seen = new HashSet<long>();
        for (int i = 0; i < n; i++) {
            queue.Enqueue((i, 1 << i, 0));
            seen.Add(((long)i << 20) | (1 << i));
        }
        while (queue.Count > 0) {
            var (node, mask, dist) = queue.Dequeue();
            if (mask == target) return dist;
            foreach (int nxt in graph[node]) {
                int nmask = mask | (1 << nxt);
                long state = ((long)nxt << 20) | (uint)nmask;
                if (seen.Add(state)) queue.Enqueue((nxt, nmask, dist + 1));
            }
        }
        return -1;
    }
}
