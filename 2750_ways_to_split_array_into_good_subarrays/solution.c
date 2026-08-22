// LeetCode 2750 - Ways to Split Array Into Good Subarrays
// https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/

#include <stdlib.h>

int numberOfGoodSubarraySplits(int* nums, int numsSize) {
    const int MOD = 1000000007;
    int* ones = (int*)malloc((size_t)numsSize * sizeof(int));
    int osz = 0;
    for (int i = 0; i < numsSize; i++)
        if (nums[i] == 1) ones[osz++] = i;
    if (osz == 0) { free(ones); return 0; }
    long long ans = 1;
    for (int i = 1; i < osz; i++)
        ans = ans * (ones[i] - ones[i - 1]) % MOD;
    free(ones);
    return (int)ans;
}
