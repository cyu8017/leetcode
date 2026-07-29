// LeetCode 1406 - Stone Game III
// https://leetcode.com/problems/stone-game-iii/

#include <stdlib.h>
#include <string.h>

char* stoneGameIII(int* stoneValue, int stoneValueSize) {
    int n = stoneValueSize;
    long long* dp = (long long*)malloc((n + 1) * sizeof(long long));
    dp[n] = 0;
    for (int i = n - 1; i >= 0; i--) {
        long long take = 0;
        dp[i] = -1000000000000000000LL;
        for (int j = i; j < i + 3 && j < n; j++) {
            take += stoneValue[j];
            long long cand = take - dp[j + 1];
            if (cand > dp[i]) dp[i] = cand;
        }
    }
    char* ans = (char*)malloc(8);
    if (dp[0] > 0) strcpy(ans, "Alice");
    else if (dp[0] < 0) strcpy(ans, "Bob");
    else strcpy(ans, "Tie");
    free(dp);
    return ans;
}
