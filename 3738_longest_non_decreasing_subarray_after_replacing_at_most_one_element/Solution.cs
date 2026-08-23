// LeetCode 3738 - Longest Non-Decreasing Subarray After Replacing at Most One Element
// https://leetcode.com/problems/longest-non-decreasing-subarray-after-replacing-at-most-one-element/

using System;

public class Solution {
    public int LongestSubarray(int[] nums) {
        int n = nums.Length;
        int[] left = new int[n], right = new int[n];
        for (int i = 0; i < n; i++) { left[i] = 1; right[i] = 1; }
        for (int i = 1; i < n; i++) {
            if (nums[i] >= nums[i - 1]) left[i] = left[i - 1] + 1;
        }
        for (int i = n - 2; i >= 0; i--) {
            if (nums[i] <= nums[i + 1]) right[i] = right[i + 1] + 1;
        }
        int ans = 0;
        foreach (int v in left) ans = Math.Max(ans, v);
        for (int i = 0; i < n; i++) {
            int a = i > 0 ? left[i - 1] : 0;
            int b = i + 1 < n ? right[i + 1] : 0;
            if (i > 0 && i + 1 < n && nums[i - 1] > nums[i + 1]) {
                ans = Math.Max(ans, Math.Max(a + 1, b + 1));
            } else {
                ans = Math.Max(ans, a + b + 1);
            }
        }
        return ans;
    }
}
