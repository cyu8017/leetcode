// LeetCode 1278 - Palindrome Partitioning III
// https://leetcode.com/problems/palindrome-partitioning-iii/

#include <stdlib.h>
#include <string.h>

int palindromePartition(char* s, int k) {
    int n = (int)strlen(s);
    int** cost = (int**)malloc((size_t)n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        cost[i] = (int*)calloc((size_t)n, sizeof(int));
    }
    for (int length = 2; length <= n; length++) {
        for (int i = 0; i + length <= n; i++) {
            int j = i + length - 1;
            cost[i][j] = (length > 2 ? cost[i + 1][j - 1] : 0) + (s[i] != s[j]);
        }
    }
    int inf = n + 1;
    int** dp = (int**)malloc((size_t)(k + 1) * sizeof(int*));
    for (int p = 0; p <= k; p++) {
        dp[p] = (int*)malloc((size_t)(n + 1) * sizeof(int));
        for (int e = 0; e <= n; e++) dp[p][e] = inf;
        dp[p][0] = 0;
    }
    for (int parts = 1; parts <= k; parts++) {
        for (int end = parts; end <= n; end++) {
            for (int start = parts - 1; start < end; start++) {
                int val = dp[parts - 1][start] + cost[start][end - 1];
                if (val < dp[parts][end]) dp[parts][end] = val;
            }
        }
    }
    int ans = dp[k][n];
    for (int i = 0; i < n; i++) free(cost[i]);
    free(cost);
    for (int p = 0; p <= k; p++) free(dp[p]);
    free(dp);
    return ans;
}
