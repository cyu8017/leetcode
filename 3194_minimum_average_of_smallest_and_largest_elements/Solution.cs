// LeetCode 3194 - Minimum Average of Smallest and Largest Elements
// https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/

using System;

public class Solution {
    public double MinimumAverage(int[] nums) {
        Array.Sort(nums);
        int n = nums.Length;
        int ans = 1 << 30;
        for (int i = 0; i < n / 2; i++) ans = Math.Min(ans, nums[i] + nums[n - i - 1]);
        return ans / 2.0;
    }
}
