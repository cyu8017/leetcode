// LeetCode 2099 - Find Subsequence of Length K With the Largest Sum
// https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

#include <stdlib.h>

typedef struct { int v, i; } Pair2099;

static int cmpPairDesc(const void* a, const void* b) {
    return ((const Pair2099*)b)->v - ((const Pair2099*)a)->v;
}

static int cmpInt(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int* maxSubsequence(int* nums, int numsSize, int k, int* returnSize) {
    Pair2099* arr = (Pair2099*)malloc((size_t)numsSize * sizeof(Pair2099));
    for (int i = 0; i < numsSize; i++) { arr[i].v = nums[i]; arr[i].i = i; }
    qsort(arr, (size_t)numsSize, sizeof(Pair2099), cmpPairDesc);
    int* idx = (int*)malloc((size_t)k * sizeof(int));
    for (int i = 0; i < k; i++) idx[i] = arr[i].i;
    qsort(idx, (size_t)k, sizeof(int), cmpInt);
    int* ans = (int*)malloc((size_t)k * sizeof(int));
    for (int i = 0; i < k; i++) ans[i] = nums[idx[i]];
    free(arr); free(idx);
    *returnSize = k;
    return ans;
}
