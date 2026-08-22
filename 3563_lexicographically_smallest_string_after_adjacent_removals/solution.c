// LeetCode 3563 - Lexicographically Smallest String After Adjacent Removals
// https://leetcode.com/problems/lexicographically-smallest-string-after-adjacent-removals/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static bool isConsec(char a, char b) {
    int d = (int)a - (int)b;
    if (d < 0) d = -d;
    return d == 1 || d == 25;
}

char* lexicographicallySmallestString(char* s) {
    int n = (int)strlen(s);
    char*** dp = (char***)malloc((size_t)(n + 1) * sizeof(char**));
    for (int i = 0; i <= n; i++) {
        dp[i] = (char**)calloc((size_t)(n + 1), sizeof(char*));
        for (int j = 0; j <= n; j++) {
            dp[i][j] = (char*)calloc(1, 1);
        }
    }
    for (int length = 1; length <= n; length++) {
        for (int i = 0; i + length <= n; i++) {
            int j = i + length;
            char* minStr = (char*)malloc((size_t)length + 1);
            minStr[0] = s[i];
            strcpy(minStr + 1, dp[i + 1][j]);
            for (int k = i + 1; k < j; k++) {
                if (isConsec(s[i], s[k]) && dp[i + 1][k][0] == '\0') {
                    char* cand = dp[k + 1][j];
                    if (strcmp(cand, minStr) < 0) {
                        free(minStr);
                        minStr = (char*)malloc(strlen(cand) + 1);
                        strcpy(minStr, cand);
                    }
                }
            }
            free(dp[i][j]);
            dp[i][j] = minStr;
        }
    }
    char* ans = (char*)malloc(strlen(dp[0][n]) + 1);
    strcpy(ans, dp[0][n]);
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= n; j++) free(dp[i][j]);
        free(dp[i]);
    }
    free(dp);
    return ans;
}
