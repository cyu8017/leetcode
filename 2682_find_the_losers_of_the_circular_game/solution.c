// LeetCode 2682 - Find the Losers of the Circular Game
// https://leetcode.com/problems/find-the-losers-of-the-circular-game/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* circularGameLosers(int n, int k, int* returnSize) {
    bool* seen = (bool*)calloc((size_t)n, sizeof(bool));
    int i = 0, step = 1;
    while (!seen[i]) {
        seen[i] = true;
        i = (i + step * k) % n;
        step++;
    }
    int* ans = (int*)malloc((size_t)n * sizeof(int));
    int sz = 0;
    for (int j = 0; j < n; j++)
        if (!seen[j]) ans[sz++] = j + 1;
    free(seen);
    *returnSize = sz;
    return ans;
}
