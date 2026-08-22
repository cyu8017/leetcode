// LeetCode 2465 - Number of Distinct Averages
// https://leetcode.com/problems/number-of-distinct-averages/

#include <stdlib.h>
#include <string.h>

static int cmp_int(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int distinctAverages(int* nums, int numsSize) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
    char seen[201] = {0};
    int l = 0, r = numsSize - 1, cnt = 0;
    while (l < r) {
        int s = nums[l] + nums[r];
        if (!seen[s]) { seen[s] = 1; cnt++; }
        l++; r--;
    }
    return cnt;
}
