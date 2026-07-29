// LeetCode 0977 - Squares of a Sorted Array
// https://leetcode.com/problems/squares-of-a-sorted-array/

#include <stdlib.h>
#include <stdlib.h>

int* sortedSquares(int* nums, int numsSize, int* returnSize) {
    int* ans = (int*)malloc((size_t)numsSize * sizeof(int));
    int i = 0, j = numsSize - 1;
    for (int k = numsSize - 1; k >= 0; k--) {
        if (abs(nums[i]) > abs(nums[j])) {
            ans[k] = nums[i] * nums[i];
            i++;
        } else {
            ans[k] = nums[j] * nums[j];
            j--;
        }
    }
    *returnSize = numsSize;
    return ans;
}
