// LeetCode 3107 - Minimum Operations to Make Median of Array Equal to K
// https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/

using System;

public class Solution {
    public long MinOperationsToMakeMedianK(int[] nums, int k) {
        Array.Sort(nums);
        int n = nums.Length, m = n >> 1;
        long ans = Math.Abs(nums[m] - k);
        if (nums[m] > k) {
            for (int i = m - 1; i >= 0 && nums[i] > k; i--) ans += nums[i] - k;
        } else {
            for (int i = m + 1; i < n && nums[i] < k; i++) ans += k - nums[i];
        }
        return ans;
    }
}
