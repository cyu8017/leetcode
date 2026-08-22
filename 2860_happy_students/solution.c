// LeetCode 2860 - Happy Students
// https://leetcode.com/problems/happy-students/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) {
    return (*(const int*)a) - (*(const int*)b);
}

int countWays(int* nums, int numsSize) {
    qsort(nums, numsSize, sizeof(int), cmp_int);
    int ans = 0;
    if (nums[0] > 0) ans++;
    for (int i = 0; i < numsSize; i++) {
        int selected = i + 1;
        if (selected > nums[i] && (i == numsSize - 1 || selected < nums[i + 1])) ans++;
    }
    return ans;
}
