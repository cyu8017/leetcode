// LeetCode 1971 - Find if Path Exists in Graph
// https://leetcode.com/problems/find-if-path-exists-in-graph/

using System.Collections.Generic;

public class Solution {
    public bool ValidPath(int n, int[][] edges, int source, int destination) {
        if (source == destination) return true;
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) { g[e[0]].Add(e[1]); g[e[1]].Add(e[0]); }
        var stack = new Stack<int>();
        var seen = new HashSet<int> { source };
        stack.Push(source);
        while (stack.Count > 0) {
            int u = stack.Pop();
            if (u == destination) return true;
            foreach (int v in g[u])
                if (seen.Add(v)) stack.Push(v);
        }
        return false;
    }
}