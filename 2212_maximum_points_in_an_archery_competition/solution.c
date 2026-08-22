// LeetCode 2212 - Maximum Points in an Archery Competition
// https://leetcode.com/problems/maximum-points-in-an-archery-competition/

#include <stdlib.h>
#include <string.h>

static int bestScore2212;
static int best2212[12];
static int* alice2212;

static void dfs2212(int i, int remain, int score, int* bob) {
    if (i == 12) {
        if (score > bestScore2212) {
            bestScore2212 = score;
            memcpy(best2212, bob, 12 * sizeof(int));
            if (remain > 0) best2212[0] += remain;
        }
        return;
    }
    dfs2212(i + 1, remain, score, bob);
    int need = alice2212[i] + 1;
    if (remain >= need) {
        bob[i] = need;
        dfs2212(i + 1, remain - need, score + i, bob);
        bob[i] = 0;
    }
}

int* maximumBobPoints(int numArrows, int* aliceArrows, int aliceArrowsSize, int* returnSize) {
    (void)aliceArrowsSize;
    bestScore2212 = -1;
    alice2212 = aliceArrows;
    int bob[12] = {0};
    dfs2212(0, numArrows, 0, bob);
    int* ans = (int*)malloc(12 * sizeof(int));
    memcpy(ans, best2212, 12 * sizeof(int));
    *returnSize = 12;
    return ans;
}
