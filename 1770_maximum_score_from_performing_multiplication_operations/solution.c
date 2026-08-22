// LeetCode 1770 - Maximum Score from Performing Multiplication Operations
// https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

#include <stdlib.h>

int maximumScore(int* nums, int numsSize, int* multipliers, int multipliersSize) {
    int n = numsSize;
    int m = multipliersSize;
    int* next = (int*)calloc((size_t)(m + 1), sizeof(int));
    int* cur = (int*)calloc((size_t)(m + 1), sizeof(int));
    for (int i = m - 1; i >= 0; i--) {
        for (int left = i; left >= 0; left--) {
            int right = n - 1 - (i - left);
            int takeLeft = nums[left] * multipliers[i] + next[left + 1];
            int takeRight = nums[right] * multipliers[i] + next[left];
            cur[left] = takeLeft > takeRight ? takeLeft : takeRight;
        }
        int* tmp = next;
        next = cur;
        cur = tmp;
    }
    int result = next[0];
    free(next);
    free(cur);
    return result;
}
