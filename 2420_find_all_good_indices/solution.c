// LeetCode 2420 - Find All Good Indices
// https://leetcode.com/problems/find-all-good-indices/

#include <stdlib.h>

int* goodIndices(int* nums, int numsSize, int k, int* returnSize) {
    int n = numsSize;
    int* dec = (int*)malloc((size_t)n * sizeof(int));
    int* inc = (int*)malloc((size_t)n * sizeof(int));
    dec[0] = 1;
    for (int i = 1; i < n; i++) dec[i] = nums[i] <= nums[i-1] ? dec[i-1] + 1 : 1;
    inc[n-1] = 1;
    for (int i = n - 2; i >= 0; i--) inc[i] = nums[i] <= nums[i+1] ? inc[i+1] + 1 : 1;
    int* ans = (int*)malloc((size_t)n * sizeof(int));
    int ac = 0;
    for (int i = k; i < n - k; i++)
        if (dec[i-1] >= k && inc[i+1] >= k) ans[ac++] = i;
    free(dec); free(inc);
    *returnSize = ac;
    return ans;
}
