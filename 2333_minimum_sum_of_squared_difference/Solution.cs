// LeetCode 2333 - Minimum Sum of Squared Difference
// https://leetcode.com/problems/minimum-sum-of-squared-difference/

using System;

public class Solution {
    public long MinSumSquareDiff(int[] nums1, int[] nums2, int k1, int k2) {
        int n = nums1.Length;
        int[] diff = new int[n];
        int maxD = 0;
        for (int i = 0; i < n; i++) {
            int d = Math.Abs(nums1[i] - nums2[i]);
            diff[i] = d;
            if (d > maxD) maxD = d;
        }
        int k = k1 + k2;
        int[] freq = new int[maxD + 1];
        foreach (int d in diff) freq[d]++;
        for (int d = maxD; d > 0 && k > 0; d--) {
            if (freq[d] == 0) continue;
            int take = freq[d];
            if (take > k) take = k;
            freq[d] -= take;
            freq[d - 1] += take;
            k -= take;
        }
        long ans = 0;
        for (int d = 0; d <= maxD; d++) ans += (long)d * d * freq[d];
        return ans;
    }
}
