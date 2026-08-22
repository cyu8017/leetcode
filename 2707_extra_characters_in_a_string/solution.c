// LeetCode 2707 - Extra Characters in a String
// https://leetcode.com/problems/extra-characters-in-a-string/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int minExtraChar(char* s, char** dictionary, int dictionarySize) {
    int n = (int)strlen(s);
    int* dp = (int*)malloc((size_t)(n + 1) * sizeof(int));
    dp[0] = 0;
    for (int i = 1; i <= n; i++) {
        dp[i] = dp[i - 1] + 1;
        for (int j = 0; j < i; j++) {
            for (int d = 0; d < dictionarySize; d++) {
                int len = (int)strlen(dictionary[d]);
                if (len == i - j && strncmp(s + j, dictionary[d], (size_t)len) == 0 && dp[j] < dp[i])
                    dp[i] = dp[j];
            }
        }
    }
    int ans = dp[n];
    free(dp);
    return ans;
}
