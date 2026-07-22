// LeetCode 1690 - Stone Game VII
// https://leetcode.com/problems/stone-game-vii/

#include <stdlib.h>

int stoneGameVII(int* stones, int stonesSize) {
    int n = stonesSize;
    int* pre = (int*)calloc((size_t)n + 1, sizeof(int));
    for (int i = 0; i < n; i++) pre[i + 1] = pre[i] + stones[i];
    int* dp = (int*)calloc((size_t)n * (size_t)n, sizeof(int));
    #define DP(i,j) dp[(i)*n+(j)]
    for (int length = 2; length <= n; length++) {
        for (int i = 0; i + length - 1 < n; i++) {
            int j = i + length - 1;
            int a = pre[j + 1] - pre[i + 1] - DP(i + 1, j);
            int b = pre[j] - pre[i] - DP(i, j - 1);
            DP(i, j) = a > b ? a : b;
        }
    }
    int ans = DP(0, n - 1);
    free(pre); free(dp);
    #undef DP
    return ans;
}
