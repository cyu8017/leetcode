// LeetCode 0956 - Tallest Billboard
// https://leetcode.com/problems/tallest-billboard/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int TallestBillboard(int[] rods) {
        var dp = new Dictionary<int, int> { [0] = 0 };
        foreach (int rod in rods) {
            var cur = dp.ToList();
            foreach (var kv in cur) {
                int diff = kv.Key, taller = kv.Value;
                int key1 = diff + rod;
                dp[key1] = Math.Max(dp.ContainsKey(key1) ? dp[key1] : 0, taller + rod);
                int nd = Math.Abs(diff - rod);
                int nt = diff >= rod ? taller : taller - diff + rod;
                dp[nd] = Math.Max(dp.ContainsKey(nd) ? dp[nd] : 0, nt);
            }
        }
        return dp.ContainsKey(0) ? dp[0] : 0;
    }
}
