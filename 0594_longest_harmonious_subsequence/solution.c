// LeetCode 0594 - Longest Harmonious Subsequence
// https://leetcode.com/problems/longest-harmonious-subsequence/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int findLHS(int* nums, int numsSize) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmpInt);
    int best = 0;
    int left = 0;
    for (int right = 0; right < numsSize; right++) {
        while (nums[right] - nums[left] > 1) {
            left++;
        }
        if (nums[right] - nums[left] == 1) {
            int len = right - left + 1;
            if (len > best) {
                best = len;
            }
        }
    }
    return best;
}
