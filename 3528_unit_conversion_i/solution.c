// LeetCode 3528 - Unit Conversion I
// https://leetcode.com/problems/unit-conversion-i/

#include <stdlib.h>

#define MOD3528 1000000007

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* baseUnitConversions(int** conversions, int conversionsSize, int* conversionsColSize, int* returnSize) {
    (void)conversionsColSize;
    int n = conversionsSize + 1;
    int** g = (int**)calloc((size_t)n, sizeof(int*));
    int** gw = (int**)calloc((size_t)n, sizeof(int*));
    int* gsz = (int*)calloc((size_t)n, sizeof(int));
    int* gcap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < conversionsSize; i++) {
        int s = conversions[i][0], t = conversions[i][1], w = conversions[i][2];
        if (gsz[s] == gcap[s]) {
            gcap[s] = gcap[s] ? gcap[s] * 2 : 2;
            g[s] = (int*)realloc(g[s], (size_t)gcap[s] * sizeof(int));
            gw[s] = (int*)realloc(gw[s], (size_t)gcap[s] * sizeof(int));
        }
        g[s][gsz[s]] = t;
        gw[s][gsz[s]] = w;
        gsz[s]++;
    }
    int* ans = (int*)calloc((size_t)n, sizeof(int));
    int* stack_s = (int*)malloc((size_t)n * sizeof(int));
    int* stack_m = (int*)malloc((size_t)n * sizeof(int));
    int top = 0;
    stack_s[top] = 0; stack_m[top] = 1; top++;
    while (top) {
        top--;
        int s = stack_s[top], mul = stack_m[top];
        ans[s] = mul;
        for (int i = 0; i < gsz[s]; i++) {
            stack_s[top] = g[s][i];
            stack_m[top] = (int)((long long)mul * gw[s][i] % MOD3528);
            top++;
        }
    }
    for (int i = 0; i < n; i++) { free(g[i]); free(gw[i]); }
    free(g); free(gw); free(gsz); free(gcap); free(stack_s); free(stack_m);
    *returnSize = n;
    return ans;
}
