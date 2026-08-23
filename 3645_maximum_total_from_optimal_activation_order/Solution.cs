// LeetCode 3645 - Maximum Total from Optimal Activation Order
// https://leetcode.com/problems/maximum-total-from-optimal-activation-order/

using System;
using System.Collections.Generic;

public class Solution {
    public long MaxTotal(int[] value, int[] limit) {
        var g = new Dictionary<int, List<int>>();
        for (int i = 0; i < value.Length; i++) {
            if (!g.ContainsKey(limit[i])) g[limit[i]] = new List<int>();
            g[limit[i]].Add(value[i]);
        }
        long ans = 0;
        foreach (var kv in g) {
            int lim = kv.Key;
            var vs = kv.Value;
            vs.Sort((a, b) => b.CompareTo(a));
            for (int i = 0; i < Math.Min(lim, vs.Count); i++) ans += vs[i];
        }
        return ans;
    }
}
