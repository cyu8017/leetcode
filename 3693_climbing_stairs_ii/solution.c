// LeetCode 3693 - Climbing Stairs II
// https://leetcode.com/problems/climbing-stairs-ii/

#include <stdlib.h>

int climbStairs(int n, int* costs, int costsSize) {
    (void)costsSize;
    const int inf = 1000000000;
    int* f = (int*)malloc((size_t)(n + 1) * sizeof(int));
    for (int i = 0; i <= n; i++) f[i] = inf;
    f[0] = 0;
    for (int i = 1; i <= n; i++) {
        int x = costs[i - 1];
        int j0 = i - 3; if (j0 < 0) j0 = 0;
        for (int j = j0; j < i; j++) {
            int v = f[j] + x + (i - j) * (i - j);
            if (v < f[i]) f[i] = v;
        }
    }
    int ans = f[n];
    free(f);
    return ans;
}
