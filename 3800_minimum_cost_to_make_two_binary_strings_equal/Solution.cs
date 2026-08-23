// LeetCode 3800 - Minimum Cost To Make Two Binary Strings Equal
// https://leetcode.com/problems/minimum-cost-to-make-two-binary-strings-equal/

using System;

public class Solution {
    public long MinimumCost(string s, string t, int flipCost, int swapCost, int crossCost) {
        long[] diff = new long[2];
        int n = s.Length;
        for (int i = 0; i < n; i++) {
            if (s[i] != t[i]) diff[s[i] - '0']++;
        }
        long ans = (diff[0] + diff[1]) * flipCost;
        long mx = Math.Max(diff[0], diff[1]);
        long mn = Math.Min(diff[0], diff[1]);
        ans = Math.Min(ans, mn * swapCost + (mx - mn) * flipCost);
        long avg = (mx + mn) / 2;
        ans = Math.Min(ans, (avg - mn) * crossCost + avg * swapCost + (mx + mn - avg * 2) * flipCost);
        return ans;
    }
}
