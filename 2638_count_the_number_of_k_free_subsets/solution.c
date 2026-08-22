// LeetCode 2638 - Count the Number of K-Free Subsets
// https://leetcode.com/problems/count-the-number-of-k-free-subsets/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

long long countTheNumOfKFreeSubsets(int* nums, int numsSize, int k) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmpInt);
    long long ans = 1;
    int* used = (int*)calloc((size_t)numsSize, sizeof(int));
    for (int rem = 0; rem < k; rem++) {
        int* g = (int*)malloc((size_t)numsSize * sizeof(int));
        int gc = 0;
        for (int i = 0; i < numsSize; i++) if (nums[i] % k == rem) g[gc++] = nums[i];
        if (gc == 0) { free(g); continue; }
        long long prevTake = 0, prevSkip = 1;
        int prevVal = -1;
        for (int i = 0; i < gc; i++) {
            int v = g[i];
            long long take, skip = prevTake + prevSkip;
            if (prevVal + k == v) take = prevSkip;
            else take = prevTake + prevSkip;
            prevTake = take; prevSkip = skip; prevVal = v;
        }
        ans *= prevTake + prevSkip;
        free(g);
    }
    free(used);
    return ans;
}
