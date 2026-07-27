// LeetCode 1048 - Longest String Chain
// https://leetcode.com/problems/longest-string-chain/

#include <stdlib.h>
#include <string.h>

static int cmp_len(const void* a, const void* b) {
    const char* sa = *(char* const*)a;
    const char* sb = *(char* const*)b;
    return (int)strlen(sa) - (int)strlen(sb);
}

static int is_pred(const char* prev, const char* cur) {
    int m = (int)strlen(prev), n = (int)strlen(cur);
    if (m + 1 != n) return 0;
    int i = 0, j = 0, skip = 0;
    while (i < m && j < n) {
        if (prev[i] == cur[j]) {
            i++;
            j++;
        } else {
            if (skip) return 0;
            skip = 1;
            j++;
        }
    }
    if (i != m) return 0;
    if (j == n) return skip == 1;
    if (j == n - 1) return skip == 0;
    return 0;
}

int longestStrChain(char** words, int wordsSize) {
    qsort(words, (size_t)wordsSize, sizeof(char*), cmp_len);
    int* dp = (int*)malloc((size_t)wordsSize * sizeof(int));
    int ans = 1;
    for (int i = 0; i < wordsSize; i++) {
        dp[i] = 1;
        for (int j = 0; j < i; j++) {
            if (is_pred(words[j], words[i]) && dp[j] + 1 > dp[i])
                dp[i] = dp[j] + 1;
        }
        if (dp[i] > ans) ans = dp[i];
    }
    free(dp);
    return ans;
}
