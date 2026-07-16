// LeetCode 0350 - Intersection of Two Arrays II
// https://leetcode.com/problems/intersection-of-two-arrays-ii/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* intersect(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    int capacity = nums1Size < nums2Size ? nums1Size : nums2Size;
    int* counts = (int*)calloc(20001, sizeof(int));
    int offset = 10000;

    for (int index = 0; index < nums1Size; index++) {
        counts[nums1[index] + offset] += 1;
    }

    int* result = (int*)malloc((size_t)capacity * sizeof(int));
    int resultSize = 0;
    for (int index = 0; index < nums2Size; index++) {
        int key = nums2[index] + offset;
        if (counts[key] > 0) {
            result[resultSize++] = nums2[index];
            counts[key] -= 1;
        }
    }

    free(counts);
    *returnSize = resultSize;
    return result;
}
