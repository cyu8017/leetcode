// LeetCode 1977 - Number of Ways to Separate Numbers
// https://leetcode.com/problems/number-of-ways-to-separate-numbers/

#include <stdlib.h>
#include <string.h>

int numberOfCombinations(char* num) {
    const int MOD = 1000000007;
    int n = (int)strlen(num);
    if (num[0] == '0') return 0;

    int** lcp = (int**)malloc((size_t)(n + 1) * sizeof(int*));
    for (int i = 0; i <= n; i++) lcp[i] = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int i = n - 1; i >= 0; i--) {
        for (int j = n - 1; j >= 0; j--) {
            if (num[i] == num[j]) lcp[i][j] = lcp[i + 1][j + 1] + 1;
        }
    }

    int** dp = (int**)malloc((size_t)(n + 1) * sizeof(int*));
    int** pref = (int**)malloc((size_t)(n + 1) * sizeof(int*));
    for (int i = 0; i <= n; i++) {
        dp[i] = (int*)calloc((size_t)(n + 1), sizeof(int));
        pref[i] = (int*)calloc((size_t)(n + 1), sizeof(int));
    }

    for (int i = 1; i <= n; i++) {
        for (int l = 1; l <= i; l++) {
            int start = i - l;
            if (num[start] == '0') {
                dp[i][l] = 0;
            } else if (start == 0) {
                dp[i][l] = 1;
            } else {
                int ways = 0;
                if (l > 1) ways = pref[start][l - 1 < start ? l - 1 : start];
                if (start >= l) {
                    int common = lcp[start - l][start];
                    int le = common >= l || num[start - l + common] < num[start + common];
                    if (le) ways = (ways + dp[start][l]) % MOD;
                }
                dp[i][l] = ways;
            }
        }
        for (int l = 1; l <= n; l++) {
            pref[i][l] = (pref[i][l - 1] + (l <= i ? dp[i][l] : 0)) % MOD;
        }
    }
    int ans = pref[n][n];
    for (int i = 0; i <= n; i++) { free(lcp[i]); free(dp[i]); free(pref[i]); }
    free(lcp); free(dp); free(pref);
    return ans;
}
