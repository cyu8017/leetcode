// LeetCode 0097 - Interleaving String
// https://leetcode.com/problems/interleaving-string/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool isInterleave(char* s1, char* s2, char* s3) {
    int m = (int)strlen(s1);
    int n = (int)strlen(s2);
    if (m + n != (int)strlen(s3)) {
        return false;
    }

    bool* dp = (bool*)calloc((size_t)(n + 1), sizeof(bool));
    dp[0] = true;

    for (int j = 1; j <= n; j++) {
        dp[j] = dp[j - 1] && s2[j - 1] == s3[j - 1];
    }

    for (int i = 1; i <= m; i++) {
        dp[0] = dp[0] && s1[i - 1] == s3[i - 1];
        for (int j = 1; j <= n; j++) {
            dp[j] = (dp[j] && s1[i - 1] == s3[i + j - 1])
                    || (dp[j - 1] && s2[j - 1] == s3[i + j - 1]);
        }
    }

    bool result = dp[n];
    free(dp);
    return result;
}
