// LeetCode 0960 - Delete Columns to Make Sorted III
// https://leetcode.com/problems/delete-columns-to-make-sorted-iii/

#include <string.h>

int minDeletionSize(char** strs, int strsSize) {
    int m = (int)strlen(strs[0]);
    int dp[100];
    for (int i = 0; i < m; i++) dp[i] = 1;
    for (int j = 0; j < m; j++) {
        for (int i = 0; i < j; i++) {
            int ok = 1;
            for (int r = 0; r < strsSize; r++) if (strs[r][i] > strs[r][j]) { ok = 0; break; }
            if (ok && dp[i] + 1 > dp[j]) dp[j] = dp[i] + 1;
        }
    }
    int mx = dp[0];
    for (int i = 1; i < m; i++) if (dp[i] > mx) mx = dp[i];
    return m - mx;
}
