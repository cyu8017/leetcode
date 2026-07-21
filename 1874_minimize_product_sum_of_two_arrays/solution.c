// LeetCode 1874 - Minimize Product Sum of Two Arrays
// https://leetcode.com/problems/minimize-product-sum-of-two-arrays/

#include <stdlib.h>

static int cmpAsc(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

static int cmpDesc(const void* a, const void* b) {
    return *(const int*)b - *(const int*)a;
}

int minProductSum(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    (void)nums2Size;
    qsort(nums1, (size_t)nums1Size, sizeof(int), cmpAsc);
    qsort(nums2, (size_t)nums1Size, sizeof(int), cmpDesc);
    int answer = 0;
    for (int i = 0; i < nums1Size; i++) answer += nums1[i] * nums2[i];
    return answer;
}
