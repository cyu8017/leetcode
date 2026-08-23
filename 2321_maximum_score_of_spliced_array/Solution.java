// LeetCode 2321 - Maximum Score Of Spliced Array
// https://leetcode.com/problems/maximum-score-of-spliced-array/

class Solution {
    public int maximumsSplicedArray(int[] nums1, int[] nums2) {
        return Math.max(kadane(nums1, nums2), kadane(nums2, nums1));
    }

    private int kadane(int[] a, int[] b) {
        int best = 0, cur = 0, sum = 0;
        for (int i = 0; i < a.length; ++i) {
            sum += a[i];
            cur += b[i] - a[i];
            if (cur < 0) cur = 0;
            best = Math.max(best, cur);
        }
        return sum + best;
    }
}
