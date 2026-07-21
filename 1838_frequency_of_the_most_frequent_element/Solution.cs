// LeetCode 1838 - Frequency of the Most Frequent Element
// https://leetcode.com/problems/frequency-of-the-most-frequent-element/

using System;

public class Solution {
    public int MaxFrequency(int[] nums, int k) {
        Array.Sort(nums);
        int left = 0;
        long windowSum = 0;
        int best = 0;
        for (int right = 0; right < nums.Length; right++) {
            windowSum += nums[right];
            while ((long)nums[right] * (right - left + 1) - windowSum > k) {
                windowSum -= nums[left];
                left++;
            }
            best = Math.Max(best, right - left + 1);
        }
        return best;
    }
}
