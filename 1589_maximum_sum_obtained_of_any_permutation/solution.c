// LeetCode 1589 - Maximum Sum Obtained of Any Permutation
// https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int maxSumRangeQuery(int* nums, int numsSize, int** requests, int requestsSize, int* requestsColSize) {
    (void)requestsColSize;
    int* diff = (int*)calloc((size_t)numsSize + 1, sizeof(int));
    for (int i = 0; i < requestsSize; i++) {
        diff[requests[i][0]]++;
        diff[requests[i][1] + 1]--;
    }
    for (int i = 1; i < numsSize; i++) diff[i] += diff[i - 1];
    qsort(nums, (size_t)numsSize, sizeof(int), cmpInt);
    qsort(diff, (size_t)numsSize, sizeof(int), cmpInt);
    long long ans = 0;
    for (int i = 0; i < numsSize; i++) ans += (long long)nums[i] * diff[i];
    free(diff);
    return (int)(ans % 1000000007LL);
}
