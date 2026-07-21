// LeetCode 1856 - Maximum Subarray Min-Product
// https://leetcode.com/problems/maximum-subarray-min-product/

#include <stdlib.h>

int maxSumMinProduct(int* nums, int numsSize) {
    const int MOD = 1000000007;
    long long* prefix = (long long*)malloc((size_t)(numsSize + 1) * sizeof(long long));
    prefix[0] = 0;
    for (int i = 0; i < numsSize; i++) prefix[i + 1] = prefix[i] + nums[i];

    int* leftBound = (int*)malloc((size_t)numsSize * sizeof(int));
    int* rightBound = (int*)malloc((size_t)numsSize * sizeof(int));
    int* stack = (int*)malloc((size_t)numsSize * sizeof(int));
    int top = 0;

    for (int i = 0; i < numsSize; i++) {
        while (top > 0 && nums[stack[top - 1]] >= nums[i]) top--;
        leftBound[i] = top > 0 ? stack[top - 1] : -1;
        stack[top++] = i;
    }

    top = 0;
    for (int i = numsSize - 1; i >= 0; i--) {
        while (top > 0 && nums[stack[top - 1]] >= nums[i]) top--;
        rightBound[i] = top > 0 ? stack[top - 1] : numsSize;
        stack[top++] = i;
    }

    long long best = 0;
    for (int i = 0; i < numsSize; i++) {
        long long total = prefix[rightBound[i]] - prefix[leftBound[i] + 1];
        long long product = total * nums[i];
        if (product > best) best = product;
    }

    free(prefix);
    free(leftBound);
    free(rightBound);
    free(stack);
    return (int)(best % MOD);
}
