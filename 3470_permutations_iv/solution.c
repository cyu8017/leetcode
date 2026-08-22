// LeetCode 3470 - Permutations IV
// https://leetcode.com/problems/permutations-iv/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* permute(int n, long long k, int* returnSize) {
    long long* fact = (long long*)malloc((size_t)(n + 1) * sizeof(long long));
    fact[0] = 1;
    for (int i = 1; i <= n; i++) {
        fact[i] = fact[i - 1] * i;
        if (fact[i] > 1000000000000000000LL) fact[i] = 1000000000000000000LL + 1;
    }
    int* used = (int*)calloc((size_t)(n + 1), sizeof(int));
    int* ans = (int*)malloc((size_t)n * sizeof(int));
    int alen = 0;
    long long kk = k;

    /* iterative construction matching Go dfs logic */
    int ok = 1;
    for (int pos = 0; pos < n && ok; pos++) {
        int chosen = 0;
        for (int x = 1; x <= n; x++) {
            if (used[x]) continue;
            if (pos > 0 && (ans[pos - 1] % 2 == x % 2)) continue;
            int rem = n - pos - 1;
            long long cnt = fact[rem];
            if (cnt >= kk) {
                used[x] = 1;
                ans[alen++] = x;
                chosen = 1;
                break;
            } else {
                kk -= cnt;
            }
        }
        if (!chosen) ok = 0;
    }
    free(fact);
    free(used);
    if (!ok) {
        free(ans);
        *returnSize = 0;
        return NULL;
    }
    *returnSize = n;
    return ans;
}
