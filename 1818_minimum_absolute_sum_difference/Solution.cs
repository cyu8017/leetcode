// LeetCode 1818 - Minimum Absolute Sum Difference
// https://leetcode.com/problems/minimum-absolute-sum-difference/

using System;

public class Solution {
    public int MinAbsoluteSumDiff(int[] nums1, int[] nums2) {
        const int MOD = 1_000_000_007;
        int n = nums1.Length;
        int[] sorted = (int[])nums1.Clone();
        Array.Sort(sorted);

        long total = 0;
        for (int i = 0; i < n; i++) total += Math.Abs(nums1[i] - nums2[i]);

        int bestGain = 0;
        for (int i = 0; i < n; i++) {
            int target = nums2[i];
            int current = Math.Abs(nums1[i] - target);
            int idx = Array.BinarySearch(sorted, target);
            if (idx < 0) idx = ~idx;
            foreach (int j in new[] { idx - 1, idx }) {
                if (j >= 0 && j < n) {
                    bestGain = Math.Max(bestGain, current - Math.Abs(sorted[j] - target));
                }
            }
        }
        return (int)((total - bestGain) % MOD);
    }
}
