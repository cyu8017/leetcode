// LeetCode 1018 - Binary Prefix Divisible By 5
// https://leetcode.com/problems/binary-prefix-divisible-by-5/

#include <stdbool.h>
#include <stdlib.h>

bool* prefixesDivBy5(int* nums, int numsSize, int* returnSize) {
    bool* ans = (bool*)malloc((size_t)numsSize * sizeof(bool));
    *returnSize = numsSize;
    int rem = 0;
    for (int i = 0; i < numsSize; i++) {
        rem = (rem * 2 + nums[i]) % 5;
        ans[i] = rem == 0;
    }
    return ans;
}
