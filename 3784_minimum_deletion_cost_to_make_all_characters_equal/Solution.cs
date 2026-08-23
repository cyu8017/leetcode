// LeetCode 3784 - Minimum Deletion Cost To Make All Characters Equal
// https://leetcode.com/problems/minimum-deletion-cost-to-make-all-characters-equal/

using System;
using System.Collections.Generic;

public class Solution {
    public long MinCost(string s, int[] cost) {
        long tot = 0;
        var g = new Dictionary<char, long>();
        for (int i = 0; i < cost.Length; i++) {
            tot += cost[i];
            if (!g.ContainsKey(s[i])) g[s[i]] = 0;
            g[s[i]] += cost[i];
        }
        long ans = tot;
        foreach (var x in g.Values) ans = Math.Min(ans, tot - x);
        return ans;
    }
}
