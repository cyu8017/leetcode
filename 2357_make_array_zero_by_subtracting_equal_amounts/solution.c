// LeetCode 2357 - Make Array Zero by Subtracting Equal Amounts
// https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

#include <stdlib.h>
#include <string.h>

static int cmpInt(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int minimumOperations(int* nums, int numsSize) {
    int* arr = (int*)malloc((size_t)numsSize * sizeof(int));
    memcpy(arr, nums, (size_t)numsSize * sizeof(int));
    qsort(arr, (size_t)numsSize, sizeof(int), cmpInt);
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        if (arr[i] > 0 && (i == 0 || arr[i] != arr[i - 1])) ans++;
    }
    free(arr);
    return ans;
}
