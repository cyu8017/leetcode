// LeetCode 3253 - Construct String with Minimum Cost (Easy)
// https://leetcode.com/problems/construct-string-with-minimum-cost-easy/

#include <stdlib.h>
#include <string.h>
#include <limits.h>

int minimumCost(char* target, char** words, int wordsSize, int* costs, int costsSize) {
    (void)costsSize;
    const long long INF = LLONG_MAX / 4;
    int n = (int)strlen(target);
    long long* dp = (long long*)malloc((size_t)(n + 1) * sizeof(long long));
    dp[0] = 0;
    for (int i = 1; i <= n; i++) dp[i] = INF;
    /* use parallel arrays as best map: keep unique words with min cost */
    char** bw = (char**)malloc((size_t)wordsSize * sizeof(char*));
    int* bc = (int*)malloc((size_t)wordsSize * sizeof(int));
    int bn = 0;
    for (int i = 0; i < wordsSize; i++) {
        int found = -1;
        for (int j = 0; j < bn; j++) {
            if (strcmp(bw[j], words[i]) == 0) { found = j; break; }
        }
        if (found < 0) { bw[bn] = words[i]; bc[bn] = costs[i]; bn++; }
        else if (costs[i] < bc[found]) bc[found] = costs[i];
    }
    for (int i = 0; i < n; i++) {
        if (dp[i] == INF) continue;
        for (int j = 0; j < bn; j++) {
            int L = (int)strlen(bw[j]);
            if (i + L <= n && strncmp(target + i, bw[j], (size_t)L) == 0) {
                if (dp[i] + bc[j] < dp[i + L]) dp[i + L] = dp[i] + bc[j];
            }
        }
    }
    int ans = dp[n] >= INF ? -1 : (int)dp[n];
    free(dp); free(bw); free(bc);
    return ans;
}
