// LeetCode 3698 - Split Array With Minimum Difference
// https://leetcode.com/problems/split-array-with-minimum-difference/

#include <stdlib.h>
#include <stdbool.h>

static long long llabs64(long long x) { return x < 0 ? -x : x; }

long long splitArray(int* nums, int numsSize) {
    int n = numsSize;
    long long* s = (long long*)malloc((size_t)n * sizeof(long long));
    bool* f = (bool*)malloc((size_t)n * sizeof(bool));
    bool* g = (bool*)malloc((size_t)n * sizeof(bool));
    for (int i = 0; i < n; i++) { f[i] = true; g[i] = true; }
    s[0] = nums[0];
    for (int i = 1; i < n; i++) {
        s[i] = s[i - 1] + nums[i];
        f[i] = f[i - 1];
        if (nums[i] <= nums[i - 1]) f[i] = false;
    }
    for (int i = n - 2; i >= 0; i--) {
        g[i] = g[i + 1];
        if (nums[i] <= nums[i + 1]) g[i] = false;
    }
    long long ans = (1LL << 62);
    int found = 0;
    for (int i = 0; i < n - 1; i++) {
        if (f[i] && g[i + 1]) {
            long long s1 = s[i], s2 = s[n - 1] - s[i];
            long long d = llabs64(s1 - s2);
            if (d < ans) ans = d;
            found = 1;
        }
    }
    free(s); free(f); free(g);
    return found ? ans : -1;
}
