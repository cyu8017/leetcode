// LeetCode 2870 - Minimum Number of Operations to Make Array Empty
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

#include <stdlib.h>

int minOperations(int* nums, int numsSize) {
    /* freq via sort */
    int* a = (int*)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) a[i] = nums[i];
    for (int i = 0; i < numsSize; i++)
        for (int j = i + 1; j < numsSize; j++)
            if (a[j] < a[i]) { int t = a[i]; a[i] = a[j]; a[j] = t; }
    int ans = 0, i = 0;
    while (i < numsSize) {
        int j = i;
        while (j < numsSize && a[j] == a[i]) j++;
        int c = j - i;
        if (c == 1) { free(a); return -1; }
        ans += (c + 2) / 3;
        i = j;
    }
    free(a);
    return ans;
}
