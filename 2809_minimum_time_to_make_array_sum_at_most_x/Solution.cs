// LeetCode 2809 - Minimum Time to Make Array Sum At Most x
// https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/

using System;

public class Solution {
    public int MinimumTime(IList<int> nums1, IList<int> nums2, int x) {
        int n = nums1.Count;
        var arr = new (int a, int b)[n];
        int sum1 = 0, sum2 = 0;
        for (int i = 0; i < n; i++) {
            arr[i] = (nums1[i], nums2[i]);
            sum1 += nums1[i];
            sum2 += nums2[i];
        }
        Array.Sort(arr, (u, v) => u.b.CompareTo(v.b));
        int[] dp = new int[n + 1];
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j >= 1; j--)
                dp[j] = Math.Max(dp[j], dp[j - 1] + arr[i].a + j * arr[i].b);
        }
        for (int t = 0; t <= n; t++) {
            if (sum1 + sum2 * t - dp[t] <= x) return t;
        }
        return -1;
    }
}
