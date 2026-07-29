// LeetCode 1438 - Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
// https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

#include <stdlib.h>

int longestSubarray(int* nums, int numsSize, int limit) {
    int* low = (int*)malloc(numsSize * sizeof(int));
    int* high = (int*)malloc(numsSize * sizeof(int));
    int lh = 0, lt = 0, hh = 0, ht = 0;
    int left = 0, answer = 0;
    for (int right = 0; right < numsSize; right++) {
        while (lh < lt && nums[low[lt - 1]] > nums[right]) lt--;
        while (hh < ht && nums[high[ht - 1]] < nums[right]) ht--;
        low[lt++] = right; high[ht++] = right;
        while (nums[high[hh]] - nums[low[lh]] > limit) {
            left++;
            if (low[lh] < left) lh++;
            if (high[hh] < left) hh++;
        }
        if (right - left + 1 > answer) answer = right - left + 1;
    }
    free(low); free(high);
    return answer;
}
