// LeetCode 2918 - Minimum Equal Sum of Two Arrays After Replacing Zeros
// https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

public class Solution {
    public long MinSum(int[] nums1, int[] nums2) {
        long s1 = 0, s2 = 0;
        int z1 = 0, z2 = 0;
        foreach (int v in nums1) {
            if (v == 0) { z1++; s1++; }
            else s1 += v;
        }
        foreach (int v in nums2) {
            if (v == 0) { z2++; s2++; }
            else s2 += v;
        }
        if (z1 == 0 && s1 < s2) return -1;
        if (z2 == 0 && s2 < s1) return -1;
        return s1 > s2 ? s1 : s2;
    }
}
