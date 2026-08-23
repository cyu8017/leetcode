// LeetCode 2771 - Longest Non-decreasing Subarray From Two Arrays
// https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/

using System;

public class Solution {
    public int MaxNonDecreasingLength(int[] nums1, int[] nums2) {
        int n = nums1.Length;
        int dp1 = 1, dp2 = 1, ans = 1;
        for (int i = 1; i < n; i++) {
            int nd1 = 1, nd2 = 1;
            if (nums1[i] >= nums1[i - 1]) nd1 = Math.Max(nd1, dp1 + 1);
            if (nums1[i] >= nums2[i - 1]) nd1 = Math.Max(nd1, dp2 + 1);
            if (nums2[i] >= nums1[i - 1]) nd2 = Math.Max(nd2, dp1 + 1);
            if (nums2[i] >= nums2[i - 1]) nd2 = Math.Max(nd2, dp2 + 1);
            dp1 = nd1;
            dp2 = nd2;
            ans = Math.Max(ans, Math.Max(dp1, dp2));
        }
        return ans;
    }
}
