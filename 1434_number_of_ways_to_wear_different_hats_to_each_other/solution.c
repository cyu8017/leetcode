// LeetCode 1434 - Number of Ways to Wear Different Hats to Each Other
// https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/

#include <stdlib.h>
#include <string.h>

int numberWays(int** hats, int hatsSize, int* hatsColSize) {
    const int MOD = 1000000007;
    int people = hatsSize;
    int wearers[41][10];
    int wcount[41] = {0};
    for (int p = 0; p < people; p++)
        for (int i = 0; i < hatsColSize[p]; i++)
            wearers[hats[p][i]][wcount[hats[p][i]]++] = p;
    int full = 1 << people;
    int* dp = (int*)calloc(full, sizeof(int));
    dp[0] = 1;
    for (int hat = 1; hat <= 40; hat++) {
        int* nxt = (int*)malloc(full * sizeof(int));
        memcpy(nxt, dp, full * sizeof(int));
        for (int mask = 0; mask < full; mask++) {
            if (!dp[mask]) continue;
            for (int i = 0; i < wcount[hat]; i++) {
                int person = wearers[hat][i];
                if (!(mask & (1 << person)))
                    nxt[mask | (1 << person)] = (nxt[mask | (1 << person)] + dp[mask]) % MOD;
            }
        }
        free(dp); dp = nxt;
    }
    int ans = dp[full - 1];
    free(dp);
    return ans;
}
