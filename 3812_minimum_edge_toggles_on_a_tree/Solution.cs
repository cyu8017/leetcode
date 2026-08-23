// LeetCode 3812 - Minimum Edge Toggles On A Tree
// https://leetcode.com/problems/minimum-edge-toggles-on-a-tree/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] MinimumFlips(int n, int[][] edges, string start, string target) {
        var g = new List<(int, int)>[n];
        for (int i = 0; i < n; i++) g[i] = new List<(int, int)>();
        for (int i = 0; i < n - 1; i++) {
            int a = edges[i][0], b = edges[i][1];
            g[a].Add((b, i));
            g[b].Add((a, i));
        }
        var ans = new List<int>();
        bool Dfs(int a, int fa) {
            bool rev = start[a] != target[a];
            foreach (var (b, i) in g[a]) {
                if (b != fa && Dfs(b, a)) {
                    ans.Add(i);
                    rev = !rev;
                }
            }
            return rev;
        }
        if (Dfs(0, -1)) return new int[] { -1 };
        ans.Sort();
        return ans.ToArray();
    }
}
