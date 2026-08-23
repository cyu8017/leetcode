// LeetCode 2016 - Maximum Difference Between Increasing Elements
// https://leetcode.com/problems/maximum-difference-between-increasing-elements/

using System;

public class Solution {
    public int MaximumDifference(int[] nums) {
        int ans = -1, mn = nums[0];
        for (int i = 1; i < nums.Length; i++) {
            if (nums[i] > mn) ans = Math.Max(ans, nums[i] - mn);
            else mn = nums[i];
        }
        return ans;
    }
}
