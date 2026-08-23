// LeetCode 2541 - Minimum Operations to Make Array Equal II
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/

class Solution {
    public long minOperations(int[] nums1, int[] nums2, int k) {
        if (k == 0) {
            for (int i = 0; i < nums1.length; i++) {
                if (nums1[i] != nums2[i]) return -1;
            }
            return 0;
        }
        long pos = 0, neg = 0;
        for (int i = 0; i < nums1.length; i++) {
            int d = nums1[i] - nums2[i];
            if (d % k != 0) return -1;
            if (d > 0) pos += d / k;
            else neg += (-d) / k;
        }
        return pos != neg ? -1 : pos;
    }
}
