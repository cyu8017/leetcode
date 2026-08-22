// LeetCode 3940 - Limit Occurrences In Sorted Array
// https://leetcode.com/problems/limit-occurrences-in-sorted-array/

#include <stdlib.h>

int* limitOccurrences(int* nums, int numsSize, int k, int* returnSize) {
    int n = numsSize;
    int cnt = 1, l = 1;
    for (int r = 1; r < n; r++) {
        if (nums[r] != nums[r - 1]) cnt = 1;
        else cnt++;
        if (cnt <= k) nums[l++] = nums[r];
    }
    *returnSize = (n == 0) ? 0 : l;
    if (n == 0) { *returnSize = 0; return nums; }
    return nums;
}
