// LeetCode 3225 - Maximum Score From Grid Operations
// https://leetcode.com/problems/maximum-score-from-grid-operations/

#include <stdlib.h>
#include <string.h>

long long maximumScore(int** grid, int gridSize, int* gridColSize) {
    (void)gridColSize;
    int n = gridSize;
    long long** prefix = malloc(n * sizeof(long long*));
    for (int j = 0; j < n; j++) {
        prefix[j] = calloc(n + 1, sizeof(long long));
        for (int i = 0; i < n; i++)
            prefix[j][i + 1] = prefix[j][i] + grid[i][j];
    }
    long long* prevPick = calloc(n + 1, sizeof(long long));
    long long* prevSkip = calloc(n + 1, sizeof(long long));
    for (int j = 1; j < n; j++) {
        long long* currPick = calloc(n + 1, sizeof(long long));
        long long* currSkip = calloc(n + 1, sizeof(long long));
        for (int curr = 0; curr <= n; curr++) {
            for (int prev = 0; prev <= n; prev++) {
                if (curr > prev) {
                    long long score = prefix[j - 1][curr] - prefix[j - 1][prev];
                    if (prevSkip[prev] + score > currPick[curr]) currPick[curr] = prevSkip[prev] + score;
                    if (prevSkip[prev] + score > currSkip[curr]) currSkip[curr] = prevSkip[prev] + score;
                } else {
                    long long score = prefix[j][prev] - prefix[j][curr];
                    if (prevPick[prev] + score > currPick[curr]) currPick[curr] = prevPick[prev] + score;
                    if (prevPick[prev] > currSkip[curr]) currSkip[curr] = prevPick[prev];
                }
            }
        }
        free(prevPick); free(prevSkip);
        prevPick = currPick; prevSkip = currSkip;
    }
    long long ans = prevPick[0];
    for (int i = 0; i <= n; i++) if (prevPick[i] > ans) ans = prevPick[i];
    for (int j = 0; j < n; j++) free(prefix[j]);
    free(prefix); free(prevPick); free(prevSkip);
    return ans;
}
