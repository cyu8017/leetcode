// LeetCode 2090 - K Radius Subarray Averages
// https://leetcode.com/problems/k-radius-subarray-averages/

#include <stdlib.h>

int* getAverages(int* nums, int numsSize, int k, int* returnSize) {
    int n = numsSize;
    int* ans = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) ans[i] = -1;
    *returnSize = n;
    if (2 * k + 1 > n) return ans;
    long long sum = 0;
    for (int i = 0; i < 2 * k + 1; i++) sum += nums[i];
    ans[k] = (int)(sum / (2 * k + 1));
    for (int i = k + 1; i + k < n; i++) {
        sum += nums[i + k] - nums[i - k - 1];
        ans[i] = (int)(sum / (2 * k + 1));
    }
    return ans;
}
