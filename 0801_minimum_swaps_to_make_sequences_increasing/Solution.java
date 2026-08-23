// LeetCode 0801 - Minimum Swaps To Make Sequences Increasing
// https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/

class Solution {
    public int minSwap(int[] nums1, int[] nums2) {
        int n = nums1.length;
        int[] swap = new int[n], keep = new int[n];
        java.util.Arrays.fill(swap, n);
        java.util.Arrays.fill(keep, n);
        swap[0] = 1;
        keep[0] = 0;
        for (int i = 1; i < n; i++) {
            if (nums1[i] > nums1[i - 1] && nums2[i] > nums2[i - 1]) {
                keep[i] = keep[i - 1];
                swap[i] = swap[i - 1] + 1;
            }
            if (nums1[i] > nums2[i - 1] && nums2[i] > nums1[i - 1]) {
                keep[i] = Math.min(keep[i], swap[i - 1]);
                swap[i] = Math.min(swap[i], keep[i - 1] + 1);
            }
        }
        return Math.min(swap[n - 1], keep[n - 1]);
    }
}
