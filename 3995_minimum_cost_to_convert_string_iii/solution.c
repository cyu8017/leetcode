// LeetCode 3995 - Minimum Cost to Convert String III
// https://leetcode.com/problems/minimum-cost-to-convert-string-iii/

#include <stdlib.h>
#include <string.h>
#include <limits.h>

int minCost(char* source, char* target, char*** rules, int rulesSize, int* rulesColSize, int* costs, int costsSize) {
    (void)rulesColSize; (void)costsSize;
    int n = (int)strlen(source);
    if ((int)strlen(target) != n) return -1;
    int* dp = (int*)malloc((size_t)(n + 1) * sizeof(int));
    for (int i = 0; i <= n; i++) dp[i] = INT_MAX;
    dp[0] = 0;
    for (int i = 0; i < n; i++) {
        if (dp[i] == INT_MAX) continue;
        if (source[i] == target[i] && dp[i] < dp[i + 1]) dp[i + 1] = dp[i];
        for (int j = 0; j < rulesSize; j++) {
            char* p = rules[j][0];
            char* r = rules[j][1];
            int plen = (int)strlen(p);
            if (i + plen > n) continue;
            int c = costs[j];
            int ok = 1;
            for (int k = 0; k < plen; k++) {
                if (r[k] != target[i + k]) { ok = 0; break; }
                if (p[k] == '*') ++c;
                else if (p[k] != source[i + k]) { ok = 0; break; }
            }
            if (ok && dp[i] <= INT_MAX - c && dp[i] + c < dp[i + plen])
                dp[i + plen] = dp[i] + c;
        }
    }
    int ans = dp[n] == INT_MAX ? -1 : dp[n];
    free(dp);
    return ans;
}
