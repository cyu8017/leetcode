// LeetCode 3756 - Concatenate Non Zero Digits And Multiply By Sum Ii
// https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/

#include <stdlib.h>
#include <string.h>

#define MX 100001
#define MOD 1000000007LL

static long long pow10arr[MX];
static int powInited = 0;

static void initPow(void) {
    if (powInited) return;
    powInited = 1;
    pow10arr[0] = 1;
    for (int i = 1; i < MX; i++) pow10arr[i] = pow10arr[i - 1] * 10 % MOD;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sumAndMultiply(char* s, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    initPow();
    int n = (int)strlen(s);
    int* sumD = (int*)calloc((size_t)(n + 1), sizeof(int));
    int* cntN0 = (int*)calloc((size_t)(n + 1), sizeof(int));
    long long* p = (long long*)calloc((size_t)(n + 1), sizeof(long long));
    for (int i = 1; i <= n; i++) {
        long long d = s[i - 1] - '0';
        sumD[i] = sumD[i - 1] + (int)d;
        cntN0[i] = cntN0[i - 1];
        if (d > 0) {
            cntN0[i]++;
            p[i] = (p[i - 1] * 10 + d) % MOD;
        } else p[i] = p[i - 1];
    }
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; i++) {
        int l = queries[i][0], r = queries[i][1];
        int n0 = cntN0[r + 1] - cntN0[l];
        long long sd = sumD[r + 1] - sumD[l];
        long long x = (p[r + 1] - p[l] * pow10arr[n0] % MOD + MOD) % MOD;
        ans[i] = (int)(x * sd % MOD);
    }
    free(sumD); free(cntN0); free(p);
    *returnSize = queriesSize;
    return ans;
}
