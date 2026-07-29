// LeetCode 0887 - Super Egg Drop
// https://leetcode.com/problems/super-egg-drop/

#include <stdlib.h>

int superEggDrop(int k, int n) {
    int* dp = (int*)calloc((size_t)k + 1, sizeof(int));
    int moves = 0;
    while (dp[k] < n) {
        moves++;
        for (int eggs = k; eggs >= 1; eggs--)
            dp[eggs] = dp[eggs] + dp[eggs - 1] + 1;
    }
    free(dp);
    return moves;
}
