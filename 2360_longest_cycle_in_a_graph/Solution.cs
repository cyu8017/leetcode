// LeetCode 2360 - Longest Cycle in a Graph
// https://leetcode.com/problems/longest-cycle-in-a-graph/

using System.Collections.Generic;

public class Solution {
    public int LongestCycle(int[] edges) {
        int n = edges.Length;
        bool[] vis = new bool[n];
        int ans = -1;
        for (int i = 0; i < n; i++) {
            if (vis[i]) continue;
            var dist = new Dictionary<int, int>();
            int cur = i, step = 0;
            while (cur != -1 && !vis[cur]) {
                vis[cur] = true;
                dist[cur] = step;
                cur = edges[cur];
                step++;
            }
            if (cur != -1 && dist.TryGetValue(cur, out int start)) {
                int cycle = step - start;
                if (cycle > ans) ans = cycle;
            }
        }
        return ans;
    }
}
