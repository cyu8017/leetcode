// LeetCode 3584 - Maximum Product of First and Last Elements of a Subsequence
// https://leetcode.com/problems/maximum-product-of-first-and-last-elements-of-a-subsequence/

using System;

public class Solution {
    public long MaximumProduct(int[] nums, int m) {
        long ans = long.MinValue;
        int mx = int.MinValue, mi = int.MaxValue;
        for (int i = m - 1; i < nums.Length; i++) {
            int x = nums[i], y = nums[i - m + 1];
            mi = Math.Min(mi, y);
            mx = Math.Max(mx, y);
            ans = Math.Max(ans, Math.Max(1L * x * mi, 1L * x * mx));
        }
        return ans;
    }
}
