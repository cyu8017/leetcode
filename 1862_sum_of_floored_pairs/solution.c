// LeetCode 1862 - Sum of Floored Pairs
// https://leetcode.com/problems/sum-of-floored-pairs/

#include <stdlib.h>

int sumOfFlooredPairs(int* nums, int numsSize) {
    const int MOD = 1000000007;
    int maxVal = nums[0];
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] > maxVal) maxVal = nums[i];
    }
    int* count = (int*)calloc((size_t)maxVal + 1, sizeof(int));
    for (int i = 0; i < numsSize; i++) count[nums[i]]++;
    int* prefix = (int*)malloc((size_t)(maxVal + 1) * sizeof(int));
    prefix[0] = count[0];
    for (int v = 1; v <= maxVal; v++) prefix[v] = prefix[v - 1] + count[v];

    long long answer = 0;
    for (int divisor = 1; divisor <= maxVal; divisor++) {
        if (count[divisor] == 0) continue;
        int quotient = 1;
        while ((long long)quotient * divisor <= maxVal) {
            int low = quotient * divisor;
            int high = (quotient + 1) * divisor - 1;
            if (high > maxVal) high = maxVal;
            int matches = prefix[high] - (low ? prefix[low - 1] : 0);
            answer = (answer + (long long)count[divisor] * matches * quotient) % MOD;
            quotient++;
        }
    }
    free(count);
    free(prefix);
    return (int)answer;
}
