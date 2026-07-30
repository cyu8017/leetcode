// LeetCode 1509 - Minimum Difference Between Largest and Smallest Value in Three Moves
// https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

using System;

public class Solution {
    public int MinDifference(int[] nums) {
        if (nums.Length <= 4) return 0;
        Array.Sort(nums);
        int ans = int.MaxValue;
        for (int i = 0; i < 4; i++) {
            ans = Math.Min(ans, nums[nums.Length - 4 + i] - nums[i]);
        }
        return ans;
    }
}
