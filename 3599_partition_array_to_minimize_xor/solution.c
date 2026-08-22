// LeetCode 3599 - Partition Array to Minimize XOR
// https://leetcode.com/problems/partition-array-to-minimize-xor/

#include <stdlib.h>
#include <limits.h>

static int imin(int a, int b) { return a < b ? a : b; }
static int imax(int a, int b) { return a > b ? a : b; }

int minXor(int* nums, int numsSize, int k) {
    int n = numsSize;
    int* g = (int*)calloc((size_t)n + 1, sizeof(int));
    for (int i = 1; i <= n; i++) g[i] = g[i - 1] ^ nums[i - 1];
    int** f = (int**)malloc((size_t)(n + 1) * sizeof(int*));
    for (int i = 0; i <= n; i++) {
        f[i] = (int*)malloc((size_t)(k + 1) * sizeof(int));
        for (int j = 0; j <= k; j++) f[i][j] = INT_MAX;
    }
    f[0][0] = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= (i < k ? i : k); j++) {
            for (int h = j - 1; h < i; h++) {
                if (f[h][j - 1] == INT_MAX) continue;
                f[i][j] = imin(f[i][j], imax(f[h][j - 1], g[i] ^ g[h]));
            }
        }
    }
    int ans = f[n][k];
    for (int i = 0; i <= n; i++) free(f[i]);
    free(f); free(g);
    return ans;
}
