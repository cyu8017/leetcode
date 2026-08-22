// LeetCode 3917 - Count Indices With Opposite Parity
// https://leetcode.com/problems/count-indices-with-opposite-parity/

#include <stdlib.h>

int* countOppositeParity(int* nums, int numsSize, int* returnSize) {
    int cnt[2] = {0, 0};
    for (int i = 0; i < numsSize; i++) cnt[nums[i] & 1]++;
    int* ans = malloc((size_t)numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        cnt[nums[i] & 1]--;
        ans[i] = cnt[(nums[i] & 1) ^ 1];
    }
    *returnSize = numsSize;
    return ans;
}
