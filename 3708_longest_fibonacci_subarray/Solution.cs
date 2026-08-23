// LeetCode 3708 - Longest Fibonacci Subarray
// https://leetcode.com/problems/longest-fibonacci-subarray/

using System;

public class Solution {
    public int LongestSubarray(int[] nums) {
        int f = 2, ans = f;
        for (int i = 2; i < nums.Length; i++) {
            if (nums[i] == nums[i - 1] + nums[i - 2]) {
                f++;
                ans = Math.Max(ans, f);
            } else f = 2;
        }
        return ans;
    }
}
