// LeetCode 3143 - Maximum Points Inside the Square
// https://leetcode.com/problems/maximum-points-inside-the-square/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaxPointsInsideSquare(int[][] points, string s) {
        var g = new SortedDictionary<int, List<int>>();
        for (int i = 0; i < points.Length; i++) {
            int key = Math.Max(Math.Max(points[i][0], -points[i][0]), Math.Max(points[i][1], -points[i][1]));
            if (!g.ContainsKey(key)) g[key] = new List<int>();
            g[key].Add(i);
        }
        bool[] vis = new bool[26];
        int ans = 0;
        foreach (var kv in g) {
            foreach (int i in kv.Value) {
                int j = s[i] - 'a';
                if (vis[j]) return ans;
                vis[j] = true;
            }
            ans += kv.Value.Count;
        }
        return ans;
    }
}
