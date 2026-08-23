// LeetCode 3132 - Find the Integer Added to Array II
// https://leetcode.com/problems/find-the-integer-added-to-array-ii/

import java.util.Arrays;

class Solution {
    public int minimumAddedInteger(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        int ans = 1 << 30;
        for (int t = 0; t < 3; t++) {
            int x = nums2[0] - nums1[t];
            if (ok(nums1, nums2, x)) ans = Math.min(ans, x);
        }
        return ans;
    }

    private boolean ok(int[] nums1, int[] nums2, int x) {
        int i = 0, j = 0, cnt = 0;
        while (i < nums1.length && j < nums2.length) {
            if (nums2[j] - nums1[i] != x) cnt++;
            else j++;
            i++;
        }
        return cnt <= 2;
    }
}
