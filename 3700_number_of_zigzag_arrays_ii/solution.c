// LeetCode 3700 - Number of ZigZag Arrays II
// https://leetcode.com/problems/number-of-zigzag-arrays-ii/

#include <stdlib.h>

int zigZagArrays(int n, int l, int r) {
    const int MOD = 1000000007;
    int m = r - l + 1;
    if (n == 1) return m % MOD;
    int* up = (int*)malloc((size_t)m * sizeof(int));
    int* down = (int*)malloc((size_t)m * sizeof(int));
    for (int j = 0; j < m; j++) { up[j] = 1; down[j] = 1; }
    for (int length = 2; length <= n; length++) {
        int* pref = (int*)calloc((size_t)(m + 1), sizeof(int));
        for (int j = 0; j < m; j++) pref[j + 1] = (pref[j] + down[j]) % MOD;
        int* nup = (int*)malloc((size_t)m * sizeof(int));
        for (int j = 0; j < m; j++) nup[j] = pref[j];
        int* suf = (int*)calloc((size_t)(m + 1), sizeof(int));
        for (int j = m - 1; j >= 0; j--) suf[j] = (suf[j + 1] + up[j]) % MOD;
        int* ndown = (int*)malloc((size_t)m * sizeof(int));
        for (int j = 0; j < m; j++) ndown[j] = suf[j + 1];
        free(up); free(down); free(pref); free(suf);
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
