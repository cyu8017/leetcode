// LeetCode 2918 - Minimum Equal Sum of Two Arrays After Replacing Zeros
// https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

long long minSum(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    long long s1 = 0, s2 = 0;
    int z1 = 0, z2 = 0;
    for (int i = 0; i < nums1Size; i++) {
        if (nums1[i] == 0) { z1++; s1++; } else s1 += nums1[i];
    }
    for (int i = 0; i < nums2Size; i++) {
        if (nums2[i] == 0) { z2++; s2++; } else s2 += nums2[i];
    }
    if (z1 == 0 && s1 < s2) return -1;
    if (z2 == 0 && s2 < s1) return -1;
    return s1 > s2 ? s1 : s2;
}
