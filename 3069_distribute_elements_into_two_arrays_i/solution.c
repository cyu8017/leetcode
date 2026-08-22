// LeetCode 3069 - Distribute Elements Into Two Arrays I
// https://leetcode.com/problems/distribute-elements-into-two-arrays-i/

#include <stdlib.h>

int* resultArray(int* nums, int numsSize, int* returnSize) {
    int* arr1 = (int*)malloc((size_t)numsSize * sizeof(int));
    int* arr2 = (int*)malloc((size_t)numsSize * sizeof(int));
    int n1 = 0, n2 = 0;
    arr1[n1++] = nums[0];
    arr2[n2++] = nums[1];
    for (int i = 2; i < numsSize; i++) {
        if (arr1[n1 - 1] > arr2[n2 - 1]) arr1[n1++] = nums[i];
        else arr2[n2++] = nums[i];
    }
    int* ans = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int i = 0; i < n1; i++) ans[i] = arr1[i];
    for (int i = 0; i < n2; i++) ans[n1 + i] = arr2[i];
    free(arr1); free(arr2);
    *returnSize = numsSize;
    return ans;
}
