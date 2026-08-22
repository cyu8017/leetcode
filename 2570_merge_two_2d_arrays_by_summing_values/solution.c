// LeetCode 2570 - Merge Two 2D Arrays by Summing Values
// https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/

#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** mergeArrays(int** nums1, int nums1Size, int* nums1ColSize, int** nums2, int nums2Size, int* nums2ColSize, int* returnSize, int** returnColumnSizes) {
    (void)nums1ColSize; (void)nums2ColSize;
    int** ans = (int**)malloc((size_t)(nums1Size + nums2Size) * sizeof(int*));
    int i = 0, j = 0, len = 0;
    while (i < nums1Size && j < nums2Size) {
        ans[len] = (int*)malloc(2 * sizeof(int));
        if (nums1[i][0] == nums2[j][0]) {
            ans[len][0] = nums1[i][0];
            ans[len][1] = nums1[i][1] + nums2[j][1];
            i++; j++;
        } else if (nums1[i][0] < nums2[j][0]) {
            ans[len][0] = nums1[i][0]; ans[len][1] = nums1[i][1]; i++;
        } else {
            ans[len][0] = nums2[j][0]; ans[len][1] = nums2[j][1]; j++;
        }
        len++;
    }
    while (i < nums1Size) {
        ans[len] = (int*)malloc(2 * sizeof(int));
        ans[len][0] = nums1[i][0]; ans[len][1] = nums1[i][1];
        i++; len++;
    }
    while (j < nums2Size) {
        ans[len] = (int*)malloc(2 * sizeof(int));
        ans[len][0] = nums2[j][0]; ans[len][1] = nums2[j][1];
        j++; len++;
    }
    *returnSize = len;
    *returnColumnSizes = (int*)malloc((size_t)len * sizeof(int));
    for (int k = 0; k < len; k++) (*returnColumnSizes)[k] = 2;
    return ans;
}
