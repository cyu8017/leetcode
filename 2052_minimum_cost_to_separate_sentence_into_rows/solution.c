// LeetCode 2052 - Minimum Cost to Separate Sentence Into Rows
// https://leetcode.com/problems/minimum-cost-to-separate-sentence-into-rows/

#include <stdlib.h>
#include <string.h>
#include <limits.h>

int minimumCost(char* sentence, int k) {
    char* copy = strdup(sentence);
    char* words[500];
    int n = 0;
    for (char* p = strtok(copy, " "); p; p = strtok(NULL, " ")) words[n++] = p;
    long long* dp = (long long*)malloc(((size_t)n + 1) * sizeof(long long));
    for (int i = 0; i <= n; i++) dp[i] = LLONG_MAX / 4;
    dp[n] = 0;
    for (int i = n - 1; i >= 0; i--) {
        int length = -1;
        for (int j = i; j < n; j++) {
            length += 1 + (int)strlen(words[j]);
            if (length > k) break;
            long long cost = 0;
            if (j < n - 1) {
                long long extra = k - length;
                cost = extra * extra;
            }
            if (cost + dp[j + 1] < dp[i]) dp[i] = cost + dp[j + 1];
        }
    }
    int ans = (int)dp[0];
    free(dp); free(copy);
    return ans;
}
