// LeetCode 3502 - Minimum Cost to Reach Every Position
// https://leetcode.com/problems/minimum-cost-to-reach-every-position/

using System;

public class Solution {
    public int[] MinCosts(int[] cost) {
        int n = cost.Length;
        int[] ans = new int[n];
        int mi = cost[0];
        for (int i = 0; i < n; i++) {
            mi = Math.Min(mi, cost[i]);
            ans[i] = mi;
        }
        return ans;
    }
}
