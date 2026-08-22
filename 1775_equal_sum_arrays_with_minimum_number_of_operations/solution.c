// LeetCode 1775 - Equal Sum Arrays With Minimum Number of Operations
// https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/

#include <stdlib.h>

static int cmp_desc(const void* a, const void* b) {
    return *(const int*)b - *(const int*)a;
}

int minOperations(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    if (nums1Size * 6 < nums2Size || nums2Size * 6 < nums1Size) {
        return -1;
    }
    int s1 = 0, s2 = 0;
    for (int i = 0; i < nums1Size; i++) {
        s1 += nums1[i];
    }
    for (int i = 0; i < nums2Size; i++) {
        s2 += nums2[i];
    }
    if (s1 == s2) {
        return 0;
    }
    int* big = nums1;
    int bigSize = nums1Size;
    int* small = nums2;
    int smallSize = nums2Size;
    if (s1 < s2) {
        big = nums2;
        bigSize = nums2Size;
        small = nums1;
        smallSize = nums1Size;
        int tmp = s1;
        s1 = s2;
        s2 = tmp;
    }
    int diff = s1 - s2;
    int total = bigSize + smallSize;
    int* gains = (int*)malloc((size_t)total * sizeof(int));
    int k = 0;
    for (int i = 0; i < bigSize; i++) {
        gains[k++] = big[i] - 1;
    }
    for (int i = 0; i < smallSize; i++) {
        gains[k++] = 6 - small[i];
    }
    qsort(gains, (size_t)total, sizeof(int), cmp_desc);
    int ops = 0;
    for (int i = 0; i < total && diff > 0; i++) {
        diff -= gains[i];
        ops++;
    }
    free(gains);
    return diff <= 0 ? ops : -1;
}
