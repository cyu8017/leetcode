// LeetCode 3105 - Longest Strictly Increasing or Strictly Decreasing Subarray
// https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

using System;

public class Solution {
    public int LongestMonotonicSubarray(int[] nums) {
        int ans = 1, t = 1;
        for (int i = 1; i < nums.Length; i++) {
            if (nums[i - 1] < nums[i]) {
                t++;
                ans = Math.Max(ans, t);
            } else t = 1;
        }
        t = 1;
        for (int i = 1; i < nums.Length; i++) {
            if (nums[i - 1] > nums[i]) {
                t++;
                ans = Math.Max(ans, t);
            } else t = 1;
        }
        return ans;
    }
}
