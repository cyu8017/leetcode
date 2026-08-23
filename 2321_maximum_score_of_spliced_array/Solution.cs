// LeetCode 2321 - Maximum Score Of Spliced Array
// https://leetcode.com/problems/maximum-score-of-spliced-array/

using System;

public class Solution {
    public int MaximumsSplicedArray(int[] nums1, int[] nums2) {
        int Kadane(int[] a, int[] b) {
            int best = 0, cur = 0, sum = 0;
            for (int i = 0; i < a.Length; ++i) {
                sum += a[i];
                cur += b[i] - a[i];
                if (cur < 0) cur = 0;
                best = Math.Max(best, cur);
            }
            return sum + best;
        }
        return Math.Max(Kadane(nums1, nums2), Kadane(nums2, nums1));
    }
}
