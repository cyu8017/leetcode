// LeetCode 0718 - Maximum Length of Repeated Subarray
// https://leetcode.com/problems/maximum-length-of-repeated-subarray/

using System;

public class Solution {
    public int FindLength(int[] nums1, int[] nums2) {
        int m = nums1.Length, n = nums2.Length, best = 0;
        int[] dp = new int[n + 1];
        for (int i = 1; i <= m; i++) {
            int[] next = new int[n + 1];
            for (int j = 1; j <= n; j++) {
                if (nums1[i - 1] == nums2[j - 1]) {
                    next[j] = dp[j - 1] + 1;
                    best = Math.Max(best, next[j]);
                }
            }
            dp = next;
        }
        return best;
    }
}
