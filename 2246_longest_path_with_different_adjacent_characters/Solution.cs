// LeetCode 2246 - Longest Path With Different Adjacent Characters
// https://leetcode.com/problems/longest-path-with-different-adjacent-characters/

using System;
using System.Collections.Generic;

public class Solution {
    int ans = 1;
    List<int>[] g;
    string s;

    int Dfs(int u) {
        int best1 = 0, best2 = 0;
        foreach (int v in g[u]) {
            int lenV = Dfs(v);
            if (s[v] == s[u]) continue;
            if (lenV > best1) { best2 = best1; best1 = lenV; }
            else if (lenV > best2) best2 = lenV;
        }
        ans = Math.Max(ans, 1 + best1 + best2);
        return 1 + best1;
    }

    public int LongestPath(int[] parent, string s) {
        int n = parent.Length;
        this.s = s;
        g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        for (int i = 1; i < n; i++) g[parent[i]].Add(i);
        ans = 1;
        Dfs(0);
        return ans;
    }
}
