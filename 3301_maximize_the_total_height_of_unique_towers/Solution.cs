// LeetCode 3301 - Maximize the Total Height of Unique Towers
// https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/

using System;

public class Solution {
    public long MaximumTotalSum(int[] maximumHeight) {
        Array.Sort(maximumHeight);
        Array.Reverse(maximumHeight);
        long ans = 0;
        long prev = (long)1e18;
        foreach (int h in maximumHeight) {
            long cur = h;
            if (cur >= prev) cur = prev - 1;
            if (cur <= 0) return -1;
            ans += cur;
            prev = cur;
        }
        return ans;
    }
}
