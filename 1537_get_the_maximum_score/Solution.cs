// LeetCode 1537 - Get the Maximum Score
// https://leetcode.com/problems/get-the-maximum-score/

using System;

public class Solution {
    public int MaxSum(int[] nums1, int[] nums2) {
        int i = 0, j = 0;
        long first = 0, second = 0;
        while (i < nums1.Length || j < nums2.Length) {
            if (j == nums2.Length || (i < nums1.Length && nums1[i] < nums2[j])) {
                first += nums1[i++];
            } else if (i == nums1.Length || nums2[j] < nums1[i]) {
                second += nums2[j++];
            } else {
                first = second = Math.Max(first, second) + nums1[i];
                i++; j++;
            }
        }
        return (int)(Math.Max(first, second) % 1000000007);
    }
}
