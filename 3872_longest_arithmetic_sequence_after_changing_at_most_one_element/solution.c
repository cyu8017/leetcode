// LeetCode 3872 - Longest Arithmetic Sequence After Changing At Most One Element
// https://leetcode.com/problems/longest-arithmetic-sequence-after-changing-at-most-one-element/

#include <stdlib.h>

int longestArithmetic(int* nums, int numsSize) {
    int n = numsSize;
    int* d = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 1; i < n; i++) d[i] = nums[i] - nums[i - 1];
    int* f = (int*)malloc((size_t)n * sizeof(int));
    int* g = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) { f[i] = 2; g[i] = 2; }
    f[0] = 1; g[n - 1] = 1;
    for (int i = 2; i < n; i++) if (d[i] == d[i - 1]) f[i] = f[i - 1] + 1;
    for (int i = n - 3; i >= 0; i--) if (d[i + 1] == d[i + 2]) g[i] = g[i + 1] + 1;
    int ans = 3;
    for (int i = 0; i < n; i++) {
        if (f[i] > ans) ans = f[i];
        if (g[i] > ans) ans = g[i];
        if (i > 0 && f[i - 1] + 1 > ans) ans = f[i - 1] + 1;
        if (i + 1 < n && g[i + 1] + 1 > ans) ans = g[i + 1] + 1;
        if (i > 0 && i < n - 1) {
            int diff = nums[i + 1] - nums[i - 1];
            if (diff % 2 == 0) {
                diff /= 2;
                int k = 3;
                if (i > 1 && diff == d[i - 1]) k += f[i - 1] - 1;
                if (i < n - 2 && diff == d[i + 2]) k += g[i + 1] - 1;
                if (k > ans) ans = k;
            }
        }
    }
    free(d); free(f); free(g);
    return ans;
}
