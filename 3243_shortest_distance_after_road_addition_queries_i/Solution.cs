// LeetCode 3243 - Shortest Distance After Road Addition Queries I
// https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/

using System.Collections.Generic;

public class Solution {
    public int[] ShortestDistanceAfterQueries(int n, int[][] queries) {
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        for (int i = 0; i < n - 1; i++) g[i].Add(i + 1);
        int Bfs(int start) {
            var q = new Queue<int>();
            q.Enqueue(start);
            bool[] vis = new bool[n];
            vis[start] = true;
            for (int d = 0;; d++) {
                int k = q.Count;
                while (k-- > 0) {
                    int u = q.Dequeue();
                    if (u == n - 1) return d;
                    foreach (int v in g[u]) {
                        if (!vis[v]) {
                            vis[v] = true;
                            q.Enqueue(v);
                        }
                    }
                }
            }
        }
        int[] ans = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            g[queries[i][0]].Add(queries[i][1]);
            ans[i] = Bfs(0);
        }
        return ans;
    }
}
