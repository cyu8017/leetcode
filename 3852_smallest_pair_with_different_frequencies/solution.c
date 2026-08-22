// LeetCode 3852 - Smallest Pair With Different Frequencies
// https://leetcode.com/problems/smallest-pair-with-different-frequencies/

#include <stdlib.h>
#include <limits.h>

int* minDistinctFreqPair(int* nums, int numsSize, int* returnSize) {
    int* keys = (int*)malloc((size_t)numsSize * sizeof(int));
    int* cnt = (int*)calloc((size_t)numsSize, sizeof(int));
    int ksz = 0;
    int x = nums[0];
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] < x) x = nums[i];
        int found = -1;
        for (int j = 0; j < ksz; j++) if (keys[j] == nums[i]) { found = j; break; }
        if (found < 0) { keys[ksz] = nums[i]; cnt[ksz] = 1; ksz++; }
        else cnt[found]++;
    }
    int cx = 0;
    for (int j = 0; j < ksz; j++) if (keys[j] == x) { cx = cnt[j]; break; }
    int minY = INT_MAX;
    for (int j = 0; j < ksz; j++) {
        if (keys[j] < minY && cnt[j] != cx) minY = keys[j];
    }
    int* ans = (int*)malloc(2 * sizeof(int));
    if (minY == INT_MAX) { ans[0] = -1; ans[1] = -1; }
    else { ans[0] = x; ans[1] = minY; }
    free(keys); free(cnt);
    *returnSize = 2;
    return ans;
}
