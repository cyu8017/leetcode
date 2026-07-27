// LeetCode 1092 - Shortest Common Supersequence
// https://leetcode.com/problems/shortest-common-supersequence/

#include <stdlib.h>
#include <string.h>

char* shortestCommonSupersequence(char* str1, char* str2) {
    int m = (int)strlen(str1);
    int n = (int)strlen(str2);
    int** dp = (int**)malloc(((size_t)m + 1) * sizeof(int*));
    for (int i = 0; i <= m; i++) {
        dp[i] = (int*)calloc((size_t)n + 1, sizeof(int));
    }
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (str1[i - 1] == str2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = dp[i - 1][j] >= dp[i][j - 1] ? dp[i - 1][j] : dp[i][j - 1];
            }
        }
    }
    char* buf = (char*)malloc((size_t)m + (size_t)n + 1);
    int len = 0;
    int i = m, j = n;
    while (i > 0 && j > 0) {
        if (str1[i - 1] == str2[j - 1]) {
            buf[len++] = str1[i - 1];
            i--;
            j--;
        } else if (dp[i - 1][j] >= dp[i][j - 1]) {
            buf[len++] = str1[i - 1];
            i--;
        } else {
            buf[len++] = str2[j - 1];
            j--;
        }
    }
    while (i > 0) {
        buf[len++] = str1[--i];
    }
    while (j > 0) {
        buf[len++] = str2[--j];
    }
    for (int a = 0, b = len - 1; a < b; a++, b--) {
        char t = buf[a];
        buf[a] = buf[b];
        buf[b] = t;
    }
    buf[len] = '\0';
    for (int k = 0; k <= m; k++) {
        free(dp[k]);
    }
    free(dp);
    return buf;
}
