// LeetCode 0656 - Coin Path
// https://leetcode.com/problems/coin-path/

#include <stdlib.h>
#include <limits.h>

int* cheapestJump(int* coins, int coinsSize, int maxJump, int* returnSize) {
    long long* cost = (long long*)malloc((size_t)coinsSize * sizeof(long long));
    int* nxt = (int*)malloc((size_t)coinsSize * sizeof(int));
    for (int i = 0; i < coinsSize; i++) { cost[i] = LLONG_MAX / 4; nxt[i] = -1; }
    if (coins[coinsSize - 1] == -1) { *returnSize = 0; free(cost); free(nxt); return NULL; }
    cost[coinsSize - 1] = coins[coinsSize - 1];
    for (int i = coinsSize - 2; i >= 0; i--) {
        if (coins[i] == -1) continue;
        for (int jump = 1; jump <= maxJump; jump++) {
            int j = i + jump;
            if (j >= coinsSize) break;
            if (cost[j] >= LLONG_MAX / 4) continue;
            long long candidate = coins[i] + cost[j];
            if (candidate < cost[i] || (candidate == cost[i] && (nxt[i] == -1 || j < nxt[i]))) {
                cost[i] = candidate;
                nxt[i] = j;
            }
        }
    }
    if (cost[0] >= LLONG_MAX / 4) { *returnSize = 0; free(cost); free(nxt); return NULL; }
    int* path = (int*)malloc((size_t)coinsSize * sizeof(int));
    int len = 0, i = 0;
    path[len++] = 1;
    while (i != coinsSize - 1) { i = nxt[i]; path[len++] = i + 1; }
    free(cost); free(nxt);
    *returnSize = len;
    return path;
}
