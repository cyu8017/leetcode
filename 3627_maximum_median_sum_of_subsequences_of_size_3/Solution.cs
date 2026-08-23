// LeetCode 3627 - Maximum Median Sum of Subsequences of Size 3
// https://leetcode.com/problems/maximum-median-sum-of-subsequences-of-size-3/

using System;

public class Solution {
    public long MaximumMedianSum(int[] nums) {
        Array.Sort(nums);
        int n = nums.Length;
        long ans = 0;
        for (int i = n / 3; i < n; i += 2) ans += nums[i];
        return ans;
    }
}
