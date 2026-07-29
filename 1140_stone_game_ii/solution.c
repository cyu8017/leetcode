// LeetCode 1140 - Stone Game II
// https://leetcode.com/problems/stone-game-ii/

#include <stdlib.h>
#include <string.h>

static int dfsSG(int i, int m, int n, int* suffix, int* memo) {
    if (i >= n) return 0;
    int key = i * (n + 1) + m;
    if (memo[key] != -1) return memo[key];
    if (i + m >= n) return memo[key] = suffix[i];
    int bestOpp = 2147483647;
    int limit = m * 2 < n - i ? m * 2 : n - i;
    for (int x = 1; x <= limit; x++) {
        int nm = x > m ? x : m;
        int v = dfsSG(i + x, nm, n, suffix, memo);
        if (v < bestOpp) bestOpp = v;
    }
    return memo[key] = suffix[i] - bestOpp;
}

int stoneGameII(int* piles, int pilesSize) {
    int n = pilesSize;
    int* suffix = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int i = n - 1; i >= 0; i--) suffix[i] = suffix[i + 1] + piles[i];
    int* memo = (int*)malloc((size_t)n * (n + 1) * sizeof(int));
    for (int i = 0; i < n * (n + 1); i++) memo[i] = -1;
    int ans = dfsSG(0, 1, n, suffix, memo);
    free(suffix); free(memo);
    return ans;
}
