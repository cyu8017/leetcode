// LeetCode 0922 - Sort Array By Parity II
// https://leetcode.com/problems/sort-array-by-parity-ii/

#include <stdlib.h>

int* sortArrayByParityII(int* nums, int numsSize, int* returnSize) {
    int* ans = (int*)malloc((size_t)numsSize * sizeof(int));
    int even = 0, odd = 1;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] % 2 == 0) { ans[even] = nums[i]; even += 2; }
        else { ans[odd] = nums[i]; odd += 2; }
    }
    *returnSize = numsSize;
    return ans;
}
