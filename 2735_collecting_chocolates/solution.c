// LeetCode 2735 - Collecting Chocolates
// https://leetcode.com/problems/collecting-chocolates/

#include <stdlib.h>

long long minCost(int* nums, int numsSize, int x) {
    int n = numsSize;
    int* best = (int*)malloc((size_t)n * sizeof(int));
    long long ans = 0;
    for (int i = 0; i < n; i++) { best[i] = nums[i]; ans += nums[i]; }
    for (int rot = 1; rot < n; rot++) {
        long long cur = 0;
        for (int i = 0; i < n; i++) {
            int v = nums[(i + rot) % n];
            if (v < best[i]) best[i] = v;
            cur += best[i];
        }
        cur += (long long)rot * x;
        if (cur < ans) ans = cur;
    }
    free(best);
    return ans;
}
