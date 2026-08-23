// LeetCode 3905 - Multi Source Flood Fill
// https://leetcode.com/problems/multi-source-flood-fill/

using System.Collections.Generic;

public class Solution {
    public int[][] ColorGrid(int n, int m, int[][] sources) {
        var ans = new int[n][];
        for (int i = 0; i < n; i++) ans[i] = new int[m];
        var q = new List<int[]>();
        foreach (var s in sources) q.Add(s);
        int[] dirs = { -1, 0, 1, 0, -1 };
        foreach (var s in q) ans[s[0]][s[1]] = s[2];
        while (q.Count > 0) {
            var vis = new SortedDictionary<(int, int), int>();
            foreach (var curr in q) {
                int r = curr[0], c = curr[1], color = curr[2];
                for (int i = 0; i < 4; i++) {
                    int x = r + dirs[i], y = c + dirs[i + 1];
                    if (x >= 0 && x < n && y >= 0 && y < m && ans[x][y] == 0) {
                        var key = (x, y);
                        if (!vis.ContainsKey(key) || color > vis[key]) vis[key] = color;
                    }
                }
            }
            q.Clear();
            foreach (var kv in vis) {
                ans[kv.Key.Item1][kv.Key.Item2] = kv.Value;
                q.Add(new int[] { kv.Key.Item1, kv.Key.Item2, kv.Value });
            }
        }
        return ans;
    }
}
