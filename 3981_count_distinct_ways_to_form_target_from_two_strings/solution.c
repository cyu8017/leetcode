// LeetCode 3981 - Count Distinct Ways to Form Target from Two Strings
// https://leetcode.com/problems/count-distinct-ways-to-form-target-from-two-strings/

#include <stdlib.h>
#include <string.h>

int countWays(char* word1, char* word2, char* target) {
    const int mod = 1000000007;
    int n1 = (int)strlen(word1);
    int n2 = (int)strlen(word2);
    int size = (n1 + 1) * (n2 + 1) * 4;
#define IDX(i, j, mask) ((((i) * (n2 + 1) + (j)) * 4) + (mask))
    int* dp = (int*)calloc((size_t)size, sizeof(int));
    int* next = (int*)calloc((size_t)size, sizeof(int));
    dp[IDX(0, 0, 0)] = 1;
    int tlen = (int)strlen(target);
    for (int t = 0; t < tlen; t++) {
        memset(next, 0, (size_t)size * sizeof(int));
        for (int j = 0; j <= n2; j++) {
            int prefix[4] = {0, 0, 0, 0};
            for (int a = 0; a < n1; a++) {
                for (int mask = 0; mask < 4; mask++) {
                    prefix[mask] += dp[IDX(a, j, mask)];
                    if (prefix[mask] >= mod) prefix[mask] -= mod;
                }
                if (word1[a] == target[t]) {
                    for (int mask = 0; mask < 4; mask++) {
                        int at = IDX(a + 1, j, mask | 1);
                        next[at] += prefix[mask];
                        if (next[at] >= mod) next[at] -= mod;
                    }
                }
            }
        }
        for (int i = 0; i <= n1; i++) {
            int prefix[4] = {0, 0, 0, 0};
            for (int b = 0; b < n2; b++) {
                for (int mask = 0; mask < 4; mask++) {
                    prefix[mask] += dp[IDX(i, b, mask)];
                    if (prefix[mask] >= mod) prefix[mask] -= mod;
                }
                if (word2[b] == target[t]) {
                    for (int mask = 0; mask < 4; mask++) {
                        int at = IDX(i, b + 1, mask | 2);
                        next[at] += prefix[mask];
                        if (next[at] >= mod) next[at] -= mod;
                    }
                }
            }
        }
        int* tmp = dp; dp = next; next = tmp;
    }
    int answer = 0;
    for (int i = 0; i <= n1; i++) {
        for (int j = 0; j <= n2; j++) {
            answer += dp[IDX(i, j, 3)];
            if (answer >= mod) answer -= mod;
        }
    }
    free(dp);
    free(next);
#undef IDX
    return answer;
}
