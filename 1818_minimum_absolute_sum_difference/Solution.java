// LeetCode 1818 - Minimum Absolute Sum Difference
// https://leetcode.com/problems/minimum-absolute-sum-difference/

import java.util.Arrays;

class Solution {
    public int minAbsoluteSumDiff(int[] nums1, int[] nums2) {
        final int mod = 1_000_000_007;
        int[] sortedNums1 = nums1.clone();
        Arrays.sort(sortedNums1);

        long total = 0;
        for (int i = 0; i < nums1.length; i++) {
            total += Math.abs((long) nums1[i] - nums2[i]);
        }

        int bestGain = 0;
        for (int i = 0; i < nums2.length; i++) {
            int target = nums2[i];
            int current = Math.abs(nums1[i] - target);
            int idx = Arrays.binarySearch(sortedNums1, target);
            if (idx < 0) {
                idx = -(idx + 1);
            }
            for (int j : new int[] {idx - 1, idx}) {
                if (j >= 0 && j < sortedNums1.length) {
                    bestGain = Math.max(bestGain, current - Math.abs(sortedNums1[j] - target));
                }
            }
        }

        return (int) ((total - bestGain) % mod);
    }
}
