// LeetCode 1775 - Equal Sum Arrays With Minimum Number of Operations
// https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/

import java.util.Arrays;

class Solution {
    public int minOperations(int[] nums1, int[] nums2) {
        if (nums1.length * 6 < nums2.length || nums2.length * 6 < nums1.length) {
            return -1;
        }
        int s1 = Arrays.stream(nums1).sum();
        int s2 = Arrays.stream(nums2).sum();
        if (s1 == s2) {
            return 0;
        }
        if (s1 < s2) {
            int[] tmpArr = nums1;
            nums1 = nums2;
            nums2 = tmpArr;
            int tmp = s1;
            s1 = s2;
            s2 = tmp;
        }
        int diff = s1 - s2;
        int[] gains = new int[nums1.length + nums2.length];
        int k = 0;
        for (int x : nums1) {
            gains[k++] = x - 1;
        }
        for (int x : nums2) {
            gains[k++] = 6 - x;
        }
        Arrays.sort(gains);
        int ops = 0;
        for (int i = gains.length - 1; i >= 0; i--) {
            if (diff <= 0) {
                break;
            }
            diff -= gains[i];
            ops++;
        }
        return diff <= 0 ? ops : -1;
    }
}
