// LeetCode 2640 - Find the Score of All Prefixes of an Array
// https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* findPrefixScore(int* nums, int numsSize, int* returnSize) {
    long long* ans = (long long*)malloc((size_t)numsSize * sizeof(long long));
    int mx = 0;
    long long sum = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > mx) mx = nums[i];
        sum += nums[i] + mx;
        ans[i] = sum;
    }
    *returnSize = numsSize;
    return ans;
}
