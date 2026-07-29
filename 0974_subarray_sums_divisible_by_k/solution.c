// LeetCode 0974 - Subarray Sums Divisible by K
// https://leetcode.com/problems/subarray-sums-divisible-by-k/

#include <stdlib.h>

int subarraysDivByK(int* nums, int numsSize, int k) {
    int* count = (int*)calloc((size_t)k, sizeof(int));
    count[0] = 1;
    int prefix = 0, ans = 0;
    for (int i = 0; i < numsSize; i++) {
        prefix = ((prefix + nums[i]) % k + k) % k;
        ans += count[prefix];
        count[prefix]++;
    }
    free(count);
    return ans;
}
