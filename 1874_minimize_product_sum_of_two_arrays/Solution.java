// LeetCode 1874 - Minimize Product Sum of Two Arrays
// https://leetcode.com/problems/minimize-product-sum-of-two-arrays/

import java.util.Arrays;

class Solution {
    public int minProductSum(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        int n = nums1.length;
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += nums1[i] * nums2[n - 1 - i];
        }
        return sum;
    }
}
