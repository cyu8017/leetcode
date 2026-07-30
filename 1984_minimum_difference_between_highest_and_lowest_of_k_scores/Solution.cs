// LeetCode 1984 - Minimum Difference Between Highest and Lowest of K Scores
// https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

using System;

public class Solution {
    public int MinimumDifference(int[] nums, int k) {
        Array.Sort(nums);
        int ans = int.MaxValue;
        for (int i = 0; i + k - 1 < nums.Length; i++)
            ans = Math.Min(ans, nums[i + k - 1] - nums[i]);
        return ans;
    }
}