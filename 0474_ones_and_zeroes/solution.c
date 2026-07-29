// LeetCode 0474 - Ones and Zeroes
// https://leetcode.com/problems/ones-and-zeroes/

#include <stdlib.h>
#include <string.h>

int findMaxForm(char** strs, int strsSize, int m, int n) {
    int** dp = (int**)malloc((size_t)(m + 1) * sizeof(int*));
    for (int i = 0; i <= m; i++) {
        dp[i] = (int*)calloc((size_t)n + 1, sizeof(int));
    }

    for (int s = 0; s < strsSize; s++) {
        int zeros = 0;
        int ones = 0;
        for (int k = 0; strs[s][k]; k++) {
            if (strs[s][k] == '0') {
                zeros++;
            } else {
                ones++;
            }
        }
        for (int zero = m; zero >= zeros; zero--) {
            for (int one = n; one >= ones; one--) {
                int candidate = dp[zero - zeros][one - ones] + 1;
                if (candidate > dp[zero][one]) {
                    dp[zero][one] = candidate;
                }
            }
        }
    }

    int answer = dp[m][n];
    for (int i = 0; i <= m; i++) {
        free(dp[i]);
    }
    free(dp);
    return answer;
}
