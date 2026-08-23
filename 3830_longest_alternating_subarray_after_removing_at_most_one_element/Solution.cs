// LeetCode 3830 - Longest Alternating Subarray After Removing At Most One Element
// https://leetcode.com/problems/longest-alternating-subarray-after-removing-at-most-one-element/

using System;

public class Solution {
    public int LongestAlternating(int[] nums) {
        int n = nums.Length;
        var l1 = new int[n];
        var l2 = new int[n];
        var r1 = new int[n];
        var r2 = new int[n];
        Array.Fill(l1, 1); Array.Fill(l2, 1); Array.Fill(r1, 1); Array.Fill(r2, 1);
        int ans = 0;
        for (int i = 1; i < n; i++) {
            if (nums[i - 1] < nums[i]) l1[i] = l2[i - 1] + 1;
            else if (nums[i - 1] > nums[i]) l2[i] = l1[i - 1] + 1;
            ans = Math.Max(ans, Math.Max(l1[i], l2[i]));
        }
        for (int i = n - 2; i >= 0; i--) {
            if (nums[i + 1] > nums[i]) r1[i] = r2[i + 1] + 1;
            else if (nums[i + 1] < nums[i]) r2[i] = r1[i + 1] + 1;
        }
        for (int i = 1; i < n - 1; i++) {
            if (nums[i - 1] < nums[i + 1]) ans = Math.Max(ans, l2[i - 1] + r2[i + 1]);
            else if (nums[i - 1] > nums[i + 1]) ans = Math.Max(ans, l1[i - 1] + r1[i + 1]);
        }
        return ans;
    }
}
