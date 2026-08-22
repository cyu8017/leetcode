// LeetCode 1223 - Dice Roll Simulation
// https://leetcode.com/problems/dice-roll-simulation/

#include <stdlib.h>
#include <string.h>

int dieSimulator(int n, int* rollMax, int rollMaxSize) {
    const int MOD = 1000000007;
    int maxRun = 0;
    for (int i = 0; i < rollMaxSize; i++) {
        if (rollMax[i] + 1 > maxRun) maxRun = rollMax[i] + 1;
    }
    int** dp = (int**)malloc(6 * sizeof(int*));
    for (int j = 0; j < 6; j++) {
        dp[j] = (int*)calloc((size_t)maxRun, sizeof(int));
        dp[j][1] = 1;
    }
    for (int step = 1; step < n; step++) {
        int totals[6];
        for (int j = 0; j < 6; j++) {
            totals[j] = 0;
            for (int run = 1; run < rollMax[j] + 1; run++) totals[j] = (totals[j] + dp[j][run]) % MOD;
        }
        int** nxt = (int**)malloc(6 * sizeof(int*));
        for (int j = 0; j < 6; j++) {
            nxt[j] = (int*)calloc((size_t)maxRun, sizeof(int));
            int sumOthers = 0;
            for (int k = 0; k < 6; k++) {
                if (k != j) sumOthers = (sumOthers + totals[k]) % MOD;
            }
            nxt[j][1] = sumOthers;
            for (int run = 2; run < rollMax[j] + 1; run++) nxt[j][run] = dp[j][run - 1];
        }
        for (int j = 0; j < 6; j++) free(dp[j]);
        free(dp);
        dp = nxt;
    }
    int ans = 0;
    for (int j = 0; j < 6; j++) {
        for (int run = 1; run < rollMax[j] + 1; run++) ans = (ans + dp[j][run]) % MOD;
        free(dp[j]);
    }
    free(dp);
    return ans;
}
