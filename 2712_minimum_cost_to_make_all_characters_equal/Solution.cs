// LeetCode 2712 - Minimum Cost to Make All Characters Equal
// https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/

using System;

public class Solution {
    public long MinimumCost(string s) {
        int n = s.Length;
        long ans = 0;
        for (int i = 1; i < n; i++) {
            if (s[i] != s[i - 1]) ans += Math.Min(i, n - i);
        }
        return ans;
    }
}
