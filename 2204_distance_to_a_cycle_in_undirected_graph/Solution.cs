// LeetCode 2204 - Distance to a Cycle in Undirected Graph
// https://leetcode.com/problems/distance-to-a-cycle-in-undirected-graph/

using System.Collections.Generic;

public class Solution {
    public int[] DistanceToCycle(int n, int[][] edges) {
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        int[] deg = new int[n];
        foreach (var e in edges) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
            deg[e[0]]++; deg[e[1]]++;
        }
        var q = new Queue<int>();
        for (int i = 0; i < n; i++) if (deg[i] == 1) q.Enqueue(i);
        bool[] onCycle = new bool[n];
        for (int i = 0; i < n; i++) onCycle[i] = true;
        while (q.Count > 0) {
            int u = q.Dequeue();
            onCycle[u] = false;
            foreach (int v in g[u]) {
                if (--deg[v] == 1) q.Enqueue(v);
            }
        }
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) ans[i] = -1;
        var qq = new Queue<int>();
        for (int i = 0; i < n; i++) if (onCycle[i]) { ans[i] = 0; qq.Enqueue(i); }
        while (qq.Count > 0) {
            int u = qq.Dequeue();
            foreach (int v in g[u]) if (ans[v] == -1) {
                ans[v] = ans[u] + 1;
                qq.Enqueue(v);
            }
        }
        return ans;
    }
}
