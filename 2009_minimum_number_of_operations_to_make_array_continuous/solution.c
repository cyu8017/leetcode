// LeetCode 2009 - Minimum Number of Operations to Make Array Continuous
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int minOperations(int* nums, int numsSize) {
    int n = numsSize;
    qsort(nums, (size_t)n, sizeof(int), cmpInt);
    int* uniq = (int*)malloc((size_t)n * sizeof(int));
    int m = 0;
    for (int i = 0; i < n; i++) {
        if (m == 0 || uniq[m - 1] != nums[i]) uniq[m++] = nums[i];
    }
    int ans = n;
    int j = 0;
    for (int i = 0; i < m; i++) {
        while (j < m && uniq[j] - uniq[i] + 1 <= n) j++;
        int have = j - i;
        if (n - have < ans) ans = n - have;
    }
    free(uniq);
    return ans;
}
