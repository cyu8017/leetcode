// LeetCode 0300 - Longest Increasing Subsequence
// https://leetcode.com/problems/longest-increasing-subsequence/

#include <stdlib.h>

int lengthOfLIS(int* nums, int numsSize) {
    int* piles = (int*)malloc((size_t)numsSize * sizeof(int));
    int pileCount = 0;

    for (int index = 0; index < numsSize; index++) {
        int num = nums[index];
        int left = 0;
        int right = pileCount;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (piles[mid] < num) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        if (left == pileCount) {
            piles[pileCount++] = num;
        } else {
            piles[left] = num;
        }
    }

    int result = pileCount;
    free(piles);
    return result;
}
