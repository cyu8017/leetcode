// LeetCode 0349 - Intersection of Two Arrays
// https://leetcode.com/problems/intersection-of-two-arrays/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* intersection(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    int capacity = nums1Size > nums2Size ? nums1Size : nums2Size;
    int* result = (int*)malloc((size_t)capacity * sizeof(int));
    int resultSize = 0;

    for (int index1 = 0; index1 < nums1Size; index1++) {
        int value = nums1[index1];
        int alreadyAdded = 0;
        for (int added = 0; added < resultSize; added++) {
            if (result[added] == value) {
                alreadyAdded = 1;
                break;
            }
        }
        if (alreadyAdded) {
            continue;
        }

        for (int index2 = 0; index2 < nums2Size; index2++) {
            if (nums2[index2] == value) {
                result[resultSize++] = value;
                break;
            }
        }
    }

    *returnSize = resultSize;
    return result;
}
