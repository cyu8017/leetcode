// LeetCode 1639 - Number of Ways to Form a Target String Given a Dictionary
// https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

#include <stdlib.h>
#include <string.h>

#define MOD 1000000007

int numWays(char** words, int wordsSize, char* target) {
    int m = (int)strlen(words[0]);
    int tlen = (int)strlen(target);
    long long* dp = (long long*)calloc((size_t)tlen + 1, sizeof(long long));
    dp[0] = 1;
    for (int j = 0; j < m; j++) {
        int count[26] = {0};
        for (int w = 0; w < wordsSize; w++) count[words[w][j] - 'a']++;
        int lim = j + 1 < tlen ? j + 1 : tlen;
        for (int i = lim; i >= 1; i--) {
            dp[i] = (dp[i] + dp[i - 1] * count[target[i - 1] - 'a']) % MOD;
        }
    }
    int ans = (int)dp[tlen];
    free(dp);
    return ans;
}
