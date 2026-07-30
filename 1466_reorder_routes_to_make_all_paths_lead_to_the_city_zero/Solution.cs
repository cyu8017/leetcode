// LeetCode 1466 - Reorder Routes To Make All Paths Lead To The City Zero
// https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

using System.Collections.Generic;
public class Solution {
    public int MinReorder(int n, int[][] connections) {
        var graph = new List<(int,int)>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<(int,int)>();
        foreach (var e in connections) { graph[e[0]].Add((e[1], 1)); graph[e[1]].Add((e[0], 0)); }
        int ans = 0;
        var stack = new Stack<int>(); var seen = new HashSet<int> { 0 };
        stack.Push(0);
        while (stack.Count > 0) {
            int node = stack.Pop();
            foreach (var (nei, cost) in graph[node])
                if (seen.Add(nei)) { stack.Push(nei); ans += cost; }
        }
        return ans;
    }
}
