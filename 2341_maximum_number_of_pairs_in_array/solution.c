// LeetCode 2341 - Maximum Number of Pairs in Array
// https://leetcode.com/problems/maximum-number-of-pairs-in-array/

#include <stdlib.h>

int* numberOfPairs(int* nums, int numsSize, int* returnSize) {
    int cnt[101] = {0};
    for (int i = 0; i < numsSize; i++) cnt[nums[i]]++;
    int pairs = 0, left = 0;
    for (int i = 0; i <= 100; i++) {
        pairs += cnt[i] / 2;
        left += cnt[i] % 2;
    }
    int* ans = (int*)malloc(2 * sizeof(int));
    ans[0] = pairs;
    ans[1] = left;
    *returnSize = 2;
    return ans;
}
