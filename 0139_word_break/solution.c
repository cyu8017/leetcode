// LeetCode 0139 - Word Break
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
bool wordBreak(char* s, char** wordDict, int wordDictSize) {
    int n = strlen(s); bool *dp = calloc(n + 1, sizeof(bool)); dp[0] = true;
    for (int i = 1; i <= n; ++i)
        for (int j = 0; j < i; ++j) if (dp[j])
            for (int w = 0; w < wordDictSize; ++w) {
                int length = strlen(wordDict[w]);
                if (length == i - j && strncmp(s + j, wordDict[w], length) == 0) { dp[i] = true; break; }
            }
    bool answer = dp[n]; free(dp); return answer;
}