// LeetCode 3731 - Find Missing Elements
// https://leetcode.com/problems/find-missing-elements/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findMissingElements(int* nums, int numsSize, int* returnSize) {
    int mn = 100, mx = 0;
    bool s[101] = {0};
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        if (x < mn) mn = x;
        if (x > mx) mx = x;
        if (x >= 0 && x <= 100) s[x] = true;
    }
    int* ans = (int*)malloc(101 * sizeof(int));
    int n = 0;
    for (int x = mn + 1; x < mx; x++) {
        if (!s[x]) ans[n++] = x;
    }
    *returnSize = n;
    return ans;
}
