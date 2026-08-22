// LeetCode 2389 - Longest Subsequence With Limited Sum
// https://leetcode.com/problems/longest-subsequence-with-limited-sum/

#include <stdlib.h>
#include <string.h>

static int cmpInt(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int* answerQueries(int* nums, int numsSize, int* queries, int queriesSize, int* returnSize) {
    int* a = (int*)malloc((size_t)numsSize * sizeof(int));
    memcpy(a, nums, (size_t)numsSize * sizeof(int));
    qsort(a, (size_t)numsSize, sizeof(int), cmpInt);
    for (int i = 1; i < numsSize; i++) a[i] += a[i - 1];
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; i++) {
        int lo = 0, hi = numsSize;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] <= queries[i]) lo = mid + 1;
            else hi = mid;
        }
        ans[i] = lo;
    }
    free(a);
    *returnSize = queriesSize;
    return ans;
}
