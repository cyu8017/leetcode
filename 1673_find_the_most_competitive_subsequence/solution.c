// LeetCode 1673 - Find the Most Competitive Subsequence
// https://leetcode.com/problems/find-the-most-competitive-subsequence/

#include <stdlib.h>

int* mostCompetitive(int* nums, int numsSize, int k, int* returnSize) {
    int* st = (int*)malloc((size_t)k * sizeof(int));
    int top = 0;
    for (int i = 0; i < numsSize; i++) {
        while (top > 0 && st[top - 1] > nums[i] && top - 1 + numsSize - i >= k) top--;
        if (top < k) st[top++] = nums[i];
    }
    *returnSize = k;
    return st;
}
