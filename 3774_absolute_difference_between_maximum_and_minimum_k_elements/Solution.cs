// LeetCode 3774 - Absolute Difference Between Maximum And Minimum K Elements
// https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements/

using System;

public class Solution {
    public int AbsDifference(int[] nums, int k) {
        Array.Sort(nums);
        int ans = 0, n = nums.Length;
        for (int i = 0; i < k; i++) ans += nums[n - i - 1] - nums[i];
        return ans;
    }
}
