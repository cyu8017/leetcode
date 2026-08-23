// LeetCode 0939 - Minimum Area Rectangle
// https://leetcode.com/problems/minimum-area-rectangle/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int MinAreaRect(int[][] points) {
        var byX = new SortedDictionary<int, List<int>>();
        foreach (var p in points) {
            if (!byX.ContainsKey(p[0])) byX[p[0]] = new List<int>();
            byX[p[0]].Add(p[1]);
        }
        var last = new Dictionary<(int, int), int>();
        long ans = long.MaxValue;
        foreach (var kv in byX) {
            int x = kv.Key;
            var ys = kv.Value;
            ys.Sort();
            for (int i = 0; i < ys.Count; i++) {
                for (int j = i + 1; j < ys.Count; j++) {
                    var key = (ys[i], ys[j]);
                    if (last.ContainsKey(key)) {
                        ans = Math.Min(ans, (long)Math.Abs(x - last[key]) * (ys[j] - ys[i]));
                    }
                    last[key] = x;
                }
            }
        }
        return ans == long.MaxValue ? 0 : (int)ans;
    }
}
