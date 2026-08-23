// LeetCode 0910 - Smallest Range II
// https://leetcode.com/problems/smallest-range-ii/

using System;

public class Solution {
    public int SmallestRangeII(int[] nums, int k) {
        Array.Sort(nums);
        int ans = nums[nums.Length - 1] - nums[0];
        for (int i = 0; i + 1 < nums.Length; i++) {
            int lo = Math.Min(nums[0] + k, nums[i + 1] - k);
            int hi = Math.Max(nums[nums.Length - 1] - k, nums[i] + k);
            ans = Math.Min(ans, hi - lo);
        }
        return ans;
    }
}
