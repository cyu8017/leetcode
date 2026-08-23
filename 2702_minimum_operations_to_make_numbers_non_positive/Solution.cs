// LeetCode 2702 - Minimum Operations to Make Numbers Non-positive
// https://leetcode.com/problems/minimum-operations-to-make-numbers-non-positive/

using System;

public class Solution {
    public int MinOperations(int[] nums, int x, int y) {
        bool Ok(int ops) {
            long extra = 0;
            foreach (int v in nums) {
                long remain = v - 1L * ops * y;
                if (remain > 0) extra += (remain + (x - y) - 1) / (x - y);
            }
            return extra <= ops;
        }
        int lo = 0, hi = 0;
        foreach (int v in nums) {
            hi = Math.Max(hi, (v + y - 1) / y);
            hi = Math.Max(hi, (v + x - 1) / x);
        }
        hi += nums.Length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (Ok(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}
