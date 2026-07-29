// LeetCode 1365 - How Many Numbers Are Smaller Than the Current Number
// https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int* smallerNumbersThanCurrent(int* nums, int numsSize, int* returnSize) {
    int* sorted = (int*)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) sorted[i] = nums[i];
    qsort(sorted, numsSize, sizeof(int), cmp_int);
    int* ans = (int*)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        int lo = 0, hi = numsSize;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (sorted[mid] < nums[i]) lo = mid + 1;
            else hi = mid;
        }
        ans[i] = lo;
    }
    free(sorted);
    *returnSize = numsSize;
    return ans;
}
