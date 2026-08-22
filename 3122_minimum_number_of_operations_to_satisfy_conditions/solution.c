// LeetCode 3122 - Minimum Number of Operations to Satisfy Conditions
// https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/

#include <stdlib.h>
#include <string.h>

int minimumOperations(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    int* f = malloc(n * 10 * sizeof(int));
    for (int i = 0; i < n * 10; i++) f[i] = 1 << 29;
    for (int i = 0; i < n; i++) {
        int cnt[10] = {0};
        for (int j = 0; j < m; j++) cnt[grid[j][i]]++;
        if (i == 0) {
            for (int j = 0; j < 10; j++) f[i * 10 + j] = m - cnt[j];
        } else {
            for (int j = 0; j < 10; j++) {
                for (int k = 0; k < 10; k++) {
                    if (j != k) {
                        int v = f[(i - 1) * 10 + k] + m - cnt[j];
                        if (v < f[i * 10 + j]) f[i * 10 + j] = v;
                    }
                }
            }
        }
    }
    int ans = 1 << 29;
    for (int j = 0; j < 10; j++) if (f[(n - 1) * 10 + j] < ans) ans = f[(n - 1) * 10 + j];
    free(f);
    return ans;
}
