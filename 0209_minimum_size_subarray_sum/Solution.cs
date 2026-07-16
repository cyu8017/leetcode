// LeetCode 0209 - Minimum Size Subarray Sum\n// https://leetcode.com/problems/\n\nusing System;

public class Solution {
    public int MinSubArrayLen(int target, int[] nums) {
        var left = 0; var sum = 0; var best = int.MaxValue;
        for (var right = 0; right < nums.Length; right++) {
            sum += nums[right];
            while (sum >= target) { best = Math.Min(best, right - left + 1); sum -= nums[left++]; }
        }
        return best == int.MaxValue ? 0 : best;
    }
}
