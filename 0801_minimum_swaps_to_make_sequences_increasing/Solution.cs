// LeetCode 0801 - Minimum Swaps To Make Sequences Increasing
// https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/

using System;

public class Solution {
    public int MinSwap(int[] nums1, int[] nums2) {
        int n = nums1.Length;
        int[] swap = new int[n], keep = new int[n];
        Array.Fill(swap, n); Array.Fill(keep, n);
        swap[0] = 1; keep[0] = 0;
        for (int i = 1; i < n; i++) {
            if (nums1[i] > nums1[i - 1] && nums2[i] > nums2[i - 1]) {
                keep[i] = keep[i - 1];
                swap[i] = swap[i - 1] + 1;
            }
            if (nums1[i] > nums2[i - 1] && nums2[i] > nums1[i - 1]) {
                keep[i] = Math.Min(keep[i], swap[i - 1]);
                swap[i] = Math.Min(swap[i], keep[i - 1] + 1);
            }
        }
        return Math.Min(swap[n - 1], keep[n - 1]);
    }
}
