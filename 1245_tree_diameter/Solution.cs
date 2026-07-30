// LeetCode 1245 - Tree Diameter
// https://leetcode.com/problems/tree-diameter/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int TreeDiameter(int[][] edges) {
        if (edges.Length == 0) return 0;
        var graph = new Dictionary<int, List<int>>();
        foreach (var e in edges) {
            if (!graph.ContainsKey(e[0])) graph[e[0]] = new List<int>();
            if (!graph.ContainsKey(e[1])) graph[e[1]] = new List<int>();
            graph[e[0]].Add(e[1]);
            graph[e[1]].Add(e[0]);
        }
        (int node, int dist) Farthest(int start) {
            var q = new Queue<(int node, int dist)>();
            var seen = new HashSet<int> { start };
            q.Enqueue((start, 0));
            (int node, int dist) last = (start, 0);
            while (q.Count > 0) {
                last = q.Dequeue();
                foreach (int v in graph[last.node]) {
                    if (seen.Add(v)) q.Enqueue((v, last.dist + 1));
                }
            }
            return last;
        }
        int endpoint = Farthest(edges[0][0]).node;
        return Farthest(endpoint).dist;
    }
}
