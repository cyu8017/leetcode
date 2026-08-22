// LeetCode 3699 - Number of ZigZag Arrays I
// https://leetcode.com/problems/number-of-zigzag-arrays-i/

#include <stdlib.h>

int zigZagArrays(int n, int l, int r) {
    const int MOD = 1000000007;
    int m = r - l + 1;
    if (n == 1) return m % MOD;
    int* up = (int*)malloc((size_t)m * sizeof(int));
    int* down = (int*)malloc((size_t)m * sizeof(int));
    for (int j = 0; j < m; j++) { up[j] = 1; down[j] = 1; }
    for (int len_ = 2; len_ <= n; len_++) {
        int* prefDown = (int*)calloc((size_t)(m + 1), sizeof(int));
        for (int j = 0; j < m; j++) prefDown[j + 1] = (prefDown[j] + down[j]) % MOD;
        int* nup = (int*)malloc((size_t)m * sizeof(int));
        for (int j = 0; j < m; j++) nup[j] = prefDown[j];
        int* sufUp = (int*)calloc((size_t)(m + 1), sizeof(int));
        for (int j = m - 1; j >= 0; j--) sufUp[j] = (sufUp[j + 1] + up[j]) % MOD;
        int* ndown = (int*)malloc((size_t)m * sizeof(int));
        for (int j = 0; j < m; j++) ndown[j] = sufUp[j + 1];
        free(up); free(down); free(prefDown); free(sufUp);
        up = nup; down = ndown;
    }
    int ans = 0;
    for (int j = 0; j < m; j++) {
        ans = (ans + up[j]) % MOD;
        ans = (ans + down[j]) % MOD;
    }
    free(up); free(down);
    return ans;
}
