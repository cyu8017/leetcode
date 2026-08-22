// LeetCode 3231 - Minimum Number of Increasing Subsequence to Be Removed
// https://leetcode.com/problems/minimum-number-of-increasing-subsequence-to-be-removed/

#include <stdlib.h>

int minOperations(int* nums, int numsSize) {
    int* g = (int*)malloc((size_t)numsSize * sizeof(int));
    int glen = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        int l = 0, r = glen;
        while (l < r) {
            int mid = (l + r) >> 1;
            if (g[mid] < x) r = mid;
            else l = mid + 1;
        }
        if (l == glen) g[glen++] = x;
        else g[l] = x;
    }
    free(g);
    return glen;
}
