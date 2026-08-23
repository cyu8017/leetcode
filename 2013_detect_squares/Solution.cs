// LeetCode 2013 - Detect Squares
// https://leetcode.com/problems/detect-squares/

using System;
using System.Collections.Generic;

public class DetectSquares {
    private readonly Dictionary<(int, int), int> cnt = new();

    public DetectSquares() {}

    public void Add(int[] point) {
        var key = (point[0], point[1]);
        if (!cnt.ContainsKey(key)) cnt[key] = 0;
        cnt[key]++;
    }

    public int Count(int[] point) {
        int x = point[0], y = point[1], ans = 0;
        foreach (var kv in cnt) {
            int px = kv.Key.Item1, py = kv.Key.Item2, c = kv.Value;
            if (px == x || py == y) continue;
            if (Math.Abs(px - x) != Math.Abs(py - y)) continue;
            int c1 = cnt.TryGetValue((px, y), out int a) ? a : 0;
            int c2 = cnt.TryGetValue((x, py), out int b) ? b : 0;
            ans += c * c1 * c2;
        }
        return ans;
    }
}
