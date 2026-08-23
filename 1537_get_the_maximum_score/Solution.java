// LeetCode 1537 - Get the Maximum Score
// https://leetcode.com/problems/get-the-maximum-score/

class Solution {
    private static final int MOD = 1_000_000_007;

    public int maxSum(int[] nums1, int[] nums2) {
        int i = 0;
        int j = 0;
        long first = 0;
        long second = 0;
        while (i < nums1.length || j < nums2.length) {
            if (j == nums2.length || (i < nums1.length && nums1[i] < nums2[j])) {
                first += nums1[i];
                i++;
            } else if (i == nums1.length || nums2[j] < nums1[i]) {
                second += nums2[j];
                j++;
            } else {
                long best = Math.max(first, second) + nums1[i];
                first = best;
                second = best;
                i++;
                j++;
            }
        }
        return (int) (Math.max(first, second) % MOD);
    }
}
