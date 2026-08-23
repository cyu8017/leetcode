// LeetCode 3486 - Longest Special Path II
// https://leetcode.com/problems/longest-special-path-ii/

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
        var pathVals = new List<int>();
        var pathDist = new List<int>();
        void Dfs(int u, int p, int dist) {
            pathVals.Add(nums[u]);
            pathDist.Add(dist);
            var freq = new Dictionary<int, int>();
            int dups = 0, left = 0;
            for (int right = 0; right < pathVals.Count; right++) {
                freq.TryGetValue(pathVals[right], out int f);
                freq[pathVals[right]] = f + 1;
                if (freq[pathVals[right]] == 2) dups++;
                while (dups > 1) {
                    if (freq[pathVals[left]] == 2) dups--;
                    freq[pathVals[left]]--;
                    left++;
                }
            }
            int length = dist - pathDist[left];
            int nodes = pathVals.Count - left;
            if (length > bestLen || (length == bestLen && nodes < bestNodes)) {
                bestLen = length;
                bestNodes = nodes;
            }
            foreach (var (to, w) in g[u]) {
                if (to == p) continue;
                Dfs(to, u, dist + w);
            }
            pathVals.RemoveAt(pathVals.Count - 1);
            pathDist.RemoveAt(pathDist.Count - 1);
        }
        Dfs(0, -1, 0);
        return new[] { bestLen, bestNodes };
    }
}
