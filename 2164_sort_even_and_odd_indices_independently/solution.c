// LeetCode 2164 - Sort Even and Odd Indices Independently
// https://leetcode.com/problems/sort-even-and-odd-indices-independently/

#include <stdlib.h>

static int cmpAsc(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }
static int cmpDesc(const void* a, const void* b) { return *(const int*)b - *(const int*)a; }

int* sortEvenOdd(int* nums, int numsSize, int* returnSize) {
    int* even = (int*)malloc((size_t)(numsSize / 2 + 1) * sizeof(int));
    int* odd = (int*)malloc((size_t)(numsSize / 2 + 1) * sizeof(int));
    int en = 0, on = 0;
    for (int i = 0; i < numsSize; i++) {
        if (i % 2 == 0) even[en++] = nums[i];
        else odd[on++] = nums[i];
    }
    qsort(even, (size_t)en, sizeof(int), cmpAsc);
    qsort(odd, (size_t)on, sizeof(int), cmpDesc);
    int* ans = (int*)malloc((size_t)numsSize * sizeof(int));
    int ei = 0, oi = 0;
    for (int i = 0; i < numsSize; i++) {
        if (i % 2 == 0) ans[i] = even[ei++];
        else ans[i] = odd[oi++];
    }
    free(even); free(odd);
    *returnSize = numsSize;
    return ans;
}
