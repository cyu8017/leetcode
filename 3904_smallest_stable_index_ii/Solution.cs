// LeetCode 3904 - Smallest Stable Index II
// https://leetcode.com/problems/smallest-stable-index-ii/

using System;

public class Solution {
    public int FirstStableIndex(int[] nums, int k) {
        int n = nums.Length;
        var right = new int[n];
        right[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) right[i] = Math.Min(right[i + 1], nums[i]);
        int left = 0;
        for (int i = 0; i < n; i++) {
            left = Math.Max(left, nums[i]);
            if (left - right[i] <= k) return i;
        }
        return -1;
    }
}
