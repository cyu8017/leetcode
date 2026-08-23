// LeetCode 2567 - Minimum Score by Changing Two Elements
// https://leetcode.com/problems/minimum-score-by-changing-two-elements/

using System;

public class Solution {
    public int MinimizeSum(int[] nums) {
        Array.Sort(nums);
        int n = nums.Length;
        int a = nums[n - 1] - nums[2];
        int b = nums[n - 3] - nums[0];
        int c = nums[n - 2] - nums[1];
        return Math.Min(a, Math.Min(b, c));
    }
}
