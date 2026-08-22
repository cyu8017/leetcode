// LeetCode 3535 - Unit Conversion II
// https://leetcode.com/problems/unit-conversion-ii/

#include <stdlib.h>

#define MOD3535 1000000007

static int qpow3535(int x, int n) {
    long long res = 1, a = x;
    while (n > 0) {
        if (n & 1) res = res * a % MOD3535;
        a = a * a % MOD3535;
        n >>= 1;
    }
    return (int)res;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* queryConversions(int** conversions, int conversionsSize, int* conversionsColSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)conversionsColSize; (void)queriesColSize;
    int n = conversionsSize + 1;
    int** g = (int**)calloc((size_t)n, sizeof(int*));
    int** gw = (int**)calloc((size_t)n, sizeof(int*));
    int* gsz = (int*)calloc((size_t)n, sizeof(int));
    int* gcap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < conversionsSize; i++) {
        int s = conversions[i][0], t = conversions[i][1], w = conversions[i][2];
        if (gsz[s] == gcap[s]) {
            gcap[s] = gcap[s] ? gcap[s] * 2 : 2;
            g[s] = realloc(g[s], (size_t)gcap[s] * sizeof(int));
            gw[s] = realloc(gw[s], (size_t)gcap[s] * sizeof(int));
        }
        g[s][gsz[s]] = t; gw[s][gsz[s]] = w; gsz[s]++;
    }
    int* res = (int*)calloc((size_t)n, sizeof(int));
    int* st = (int*)malloc((size_t)n * 2 * sizeof(int));
    int top = 0;
    st[top++] = 0; st[top++] = 1;
    while (top) {
        int mul = st[--top], s = st[--top];
        res[s] = mul;
        for (int i = 0; i < gsz[s]; i++) {
            st[top++] = g[s][i];
            st[top++] = (int)((long long)mul * gw[s][i] % MOD3535);
        }
    }
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; i++) {
        ans[i] = (int)((long long)res[queries[i][1]] * qpow3535(res[queries[i][0]], MOD3535 - 2) % MOD3535);
    }
    for (int i = 0; i < n; i++) { free(g[i]); free(gw[i]); }
    free(g); free(gw); free(gsz); free(gcap); free(res); free(st);
    *returnSize = queriesSize;
    return ans;
}
