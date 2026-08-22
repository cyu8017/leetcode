// LeetCode 2430 - Maximum Deletions on a String
// https://leetcode.com/problems/maximum-deletions-on-a-string/

#include <stdlib.h>
#include <string.h>

int deleteString(char* s) {
    int n = (int)strlen(s);
    int** lcp = (int**)malloc((size_t)(n + 1) * sizeof(int*));
    for (int i = 0; i <= n; i++) lcp[i] = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int i = n - 1; i >= 0; i--)
        for (int j = n - 1; j >= 0; j--)
            if (s[i] == s[j]) lcp[i][j] = lcp[i + 1][j + 1] + 1;
    int* dp = (int*)malloc((size_t)n * sizeof(int));
    for (int i = n - 1; i >= 0; i--) {
        dp[i] = 1;
        for (int len = 1; i + 2 * len <= n; len++) {
            if (lcp[i][i + len] >= len && 1 + dp[i + len] > dp[i])
                dp[i] = 1 + dp[i + len];
        }
    }
    int ans = dp[0];
    for (int i = 0; i <= n; i++) free(lcp[i]);
    free(lcp); free(dp);
    return ans;
}
