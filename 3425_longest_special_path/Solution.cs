// LeetCode 3425 - Longest Special Path
// https://leetcode.com/problems/longest-special-path/

using System.Collections.Generic;

public class Solution {
    public int[] LongestSpecialPath(int[][] edges, int[] nums) {
        int n = nums.Length;
        var g = new List<(int to, int w)>[n];
        for (int i = 0; i < n; i++) g[i] = new List<(int, int)>();
        foreach (var e in edges) {
            g[e[0]].Add((e[1], e[2]));
            g[e[1]].Add((e[0], e[2]));
        }
        int bestLen = 0, bestNodes = 1;
        var last = new Dictionary<int, int>();
        var path = new List<int>();
        void Dfs(int u, int p, int dist, int left) {
            int prevPos = -1;
            bool seen = last.ContainsKey(nums[u]);
            if (seen) prevPos = last[nums[u]];
            last[nums[u]] = path.Count;
            int newLeft = left;
            if (seen && prevPos >= left) newLeft = prevPos + 1;
            path.Add(dist);
            int length = dist - path[newLeft];
            int nodes = path.Count - newLeft;
            if (length > bestLen || (length == bestLen && nodes < bestNodes)) {
                bestLen = length;
                bestNodes = nodes;
            }
            foreach (var (to, w) in g[u]) {
                if (to == p) continue;
                Dfs(to, u, dist + w, newLeft);
            }
            path.RemoveAt(path.Count - 1);
            if (seen) last[nums[u]] = prevPos;
            else last.Remove(nums[u]);
        }
        Dfs(0, -1, 0, 0);
        return new[] { bestLen, bestNodes };
    }
}
