#define _POSIX_C_SOURCE 200809L
// LeetCode 0943 - Find the Shortest Superstring
// https://leetcode.com/problems/find-the-shortest-superstring/

#include <stdlib.h>
#include <string.h>

char* shortestSuperstring(char** words, int wordsSize) {
    int n = wordsSize;
    int overlap[12][12] = {{0}};
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) continue;
            int la = (int)strlen(words[i]), lb = (int)strlen(words[j]);
            for (int k = la < lb ? la : lb; k > 0; k--) {
                if (strncmp(words[i] + la - k, words[j], (size_t)k) == 0) {
                    overlap[i][j] = k;
                    break;
                }
            }
        }
    }
    int N = 1 << n;
    char*** dp = (char***)malloc((size_t)N * sizeof(char**));
    for (int m = 0; m < N; m++) {
        dp[m] = (char**)calloc((size_t)n, sizeof(char*));
    }
    for (int i = 0; i < n; i++) {
        dp[1 << i][i] = strdup(words[i]);
    }
    for (int mask = 0; mask < N; mask++) {
        for (int last = 0; last < n; last++) {
            if (!(mask & (1 << last)) || !dp[mask][last]) continue;
            for (int nxt = 0; nxt < n; nxt++) {
                if (mask & (1 << nxt)) continue;
                int ov = overlap[last][nxt];
                int len = (int)strlen(dp[mask][last]) + (int)strlen(words[nxt]) - ov;
                char* cand = (char*)malloc((size_t)(len + 1));
                strcpy(cand, dp[mask][last]);
                strcat(cand, words[nxt] + ov);
                int nmask = mask | (1 << nxt);
                if (!dp[nmask][nxt] || strlen(cand) < strlen(dp[nmask][nxt])) {
                    free(dp[nmask][nxt]);
                    dp[nmask][nxt] = cand;
                } else free(cand);
            }
        }
    }
    int full = N - 1;
    char* best = NULL;
    for (int i = 0; i < n; i++) {
        if (dp[full][i] && (!best || strlen(dp[full][i]) < strlen(best))) best = dp[full][i];
    }
    char* ans = strdup(best ? best : "");
    for (int m = 0; m < N; m++) {
        for (int i = 0; i < n; i++) free(dp[m][i]);
        free(dp[m]);
    }
    free(dp);
    return ans;
}
