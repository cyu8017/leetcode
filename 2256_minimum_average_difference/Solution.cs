// LeetCode 2256 - Minimum Average Difference
// https://leetcode.com/problems/minimum-average-difference/

using System;

public class Solution {
    public int MinimumAverageDifference(int[] nums) {
        int n = nums.Length;
        long total = 0;
        foreach (int v in nums) total += v;
        long left = 0, bestDiff = long.MaxValue;
        int bestIdx = 0;
        for (int i = 0; i < n; i++) {
            left += nums[i];
            long leftAvg = left / (i + 1);
            long rightAvg = 0;
            if (i != n - 1) rightAvg = (total - left) / (n - i - 1);
            long diff = Math.Abs(leftAvg - rightAvg);
            if (diff < bestDiff) { bestDiff = diff; bestIdx = i; }
        }
        return bestIdx;
    }
}
