// LeetCode 2574 - Left and Right Sum Differences
// https://leetcode.com/problems/left-and-right-sum-differences/

using System;

public class Solution {
    public int[] LeftRightDifference(int[] nums) {
        int total = 0;
        foreach (int x in nums) total += x;
        int[] ans = new int[nums.Length];
        int left = 0;
        for (int i = 0; i < nums.Length; ++i) {
            int right = total - left - nums[i];
            ans[i] = Math.Abs(left - right);
            left += nums[i];
        }
        return ans;
    }
}
