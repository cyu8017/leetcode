// LeetCode 1848 - Minimum Distance to the Target Element
// https://leetcode.com/problems/minimum-distance-to-the-target-element/

using System;

public class Solution {
    public int GetMinDistance(int[] nums, int target, int start) {
        int best = nums.Length;
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] == target) best = Math.Min(best, Math.Abs(i - start));
        }
        return best;
    }
}
