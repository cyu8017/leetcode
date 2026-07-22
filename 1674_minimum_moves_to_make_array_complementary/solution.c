// LeetCode 1674 - Minimum Moves to Make Array Complementary
// https://leetcode.com/problems/minimum-moves-to-make-array-complementary/

#include <stdlib.h>

int minMoves(int* nums, int numsSize, int limit) {
    int* d = (int*)calloc((size_t)(2 * limit + 2), sizeof(int));
    int n = numsSize;
    for (int i = 0; i < n / 2; i++) {
        int a = nums[i], b = nums[n - 1 - i];
        int lo = (a < b ? a : b) + 1;
        int hi = (a > b ? a : b) + limit;
        int s = a + b;
        d[2] += 2;
        d[lo] -= 1;
        d[s] -= 1;
        d[s + 1] += 1;
        d[hi + 1] += 1;
    }
    int ans = n, cur = 0;
    for (int s = 2; s <= 2 * limit; s++) {
        cur += d[s];
        if (cur < ans) ans = cur;
    }
    free(d);
    return ans;
}
