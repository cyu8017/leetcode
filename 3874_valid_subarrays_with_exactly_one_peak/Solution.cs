// LeetCode 3874 - Valid Subarrays With Exactly One Peak
// https://leetcode.com/problems/valid-subarrays-with-exactly-one-peak/

using System;
using System.Collections.Generic;

public class Solution {
    public long ValidSubarrays(int[] nums, int k) {
        int n = nums.Length;
        var peaks = new List<int>();
        for (int i = 1; i < n - 1; i++) {
            if (nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) peaks.Add(i);
        }
        long ans = 0;
        for (int j = 0; j < peaks.Count; j++) {
            int p = peaks[j];
            int leftMin = Math.Max(p - k, 0);
            if (j > 0) leftMin = Math.Max(leftMin, peaks[j - 1] + 1);
            int rightMax = Math.Min(p + k, n - 1);
            if (j < peaks.Count - 1) rightMax = Math.Min(rightMax, peaks[j + 1] - 1);
            ans += (long)(p - leftMin + 1) * (rightMax - p + 1);
        }
        return ans;
    }
}
