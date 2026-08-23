// LeetCode 3176 - Find the Maximum Length of a Good Subsequence I
// https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/

using System;

public class Solution {
    public int MaximumLength(int[] nums, int k) {
        int n = nums.Length;
        int[][] f = new int[n][];
        for (int i = 0; i < n; i++) f[i] = new int[k + 1];
        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int h = 0; h <= k; h++) {
                for (int j = 0; j < i; j++) {
                    if (nums[i] == nums[j]) f[i][h] = Math.Max(f[i][h], f[j][h]);
                    else if (h > 0) f[i][h] = Math.Max(f[i][h], f[j][h - 1]);
                }
                f[i][h]++;
            }
            ans = Math.Max(ans, f[i][k]);
        }
        return ans;
    }
}
