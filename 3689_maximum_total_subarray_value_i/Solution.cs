// LeetCode 3689 - Maximum Total Subarray Value I
// https://leetcode.com/problems/maximum-total-subarray-value-i/

using System;

public class Solution {
    public long MaxTotalValue(int[] nums, int k) {
        int mn = nums[0], mx = nums[0];
        foreach (int x in nums) {
            mn = Math.Min(mn, x);
            mx = Math.Max(mx, x);
        }
        return 1L * k * (mx - mn);
    }
}
