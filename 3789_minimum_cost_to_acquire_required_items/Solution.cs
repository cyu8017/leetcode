// LeetCode 3789 - Minimum Cost To Acquire Required Items
// https://leetcode.com/problems/minimum-cost-to-acquire-required-items/

using System;

public class Solution {
    public long MinimumCost(int cost1, int cost2, int costBoth, int need1, int need2) {
        long a = (long)need1 * cost1 + (long)need2 * cost2;
        long b = (long)costBoth * Math.Max(need1, need2);
        int mn = Math.Min(need1, need2);
        long c = (long)costBoth * mn + (long)(need1 - mn) * cost1 + (long)(need2 - mn) * cost2;
        return Math.Min(a, Math.Min(b, c));
    }
}
