// LeetCode 2561 - Rearranging Fruits
// https://leetcode.com/problems/rearranging-fruits/

using System;
using System.Collections.Generic;

public class Solution {
    public long MinCost(int[] basket1, int[] basket2) {
        var freq = new Dictionary<int, int>();
        int mn = int.MaxValue;
        foreach (int x in basket1) {
            freq[x] = freq.GetValueOrDefault(x, 0) + 1;
            mn = Math.Min(mn, x);
        }
        foreach (int x in basket2) {
            freq[x] = freq.GetValueOrDefault(x, 0) - 1;
            mn = Math.Min(mn, x);
        }
        var extra = new List<int>();
        foreach (var kv in freq) {
            if (kv.Value % 2 != 0) return -1;
            for (int i = 0; i < Math.Abs(kv.Value) / 2; ++i) extra.Add(kv.Key);
        }
        extra.Sort();
        long ans = 0;
        for (int i = 0; i < extra.Count / 2; ++i) {
            long a = extra[i];
            long b = 2L * mn;
            ans += Math.Min(a, b);
        }
        return ans;
    }
}
