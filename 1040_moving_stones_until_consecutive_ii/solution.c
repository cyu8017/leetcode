// LeetCode 1040 - Moving Stones Until Consecutive II
// https://leetcode.com/problems/moving-stones-until-consecutive-ii/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int* numMovesStonesII(int* stones, int stonesSize, int* returnSize) {
    qsort(stones, (size_t)stonesSize, sizeof(int), cmp_int);
    int n = stonesSize;
    int maxMoves = stones[n - 1] - stones[1] - n + 2;
    int alt = stones[n - 2] - stones[0] - n + 2;
    if (alt > maxMoves) maxMoves = alt;
    int minMoves = maxMoves;
    int i = 0;
    for (int j = 0; j < n; j++) {
        while (stones[j] - stones[i] + 1 > n) i++;
        int inside = j - i + 1;
        int cand;
        if (inside == n - 1 && stones[j] - stones[i] + 1 == n - 1) cand = 2;
        else cand = n - inside;
        if (cand < minMoves) minMoves = cand;
    }
    int* ans = (int*)malloc(2 * sizeof(int));
    ans[0] = minMoves;
    ans[1] = maxMoves;
    *returnSize = 2;
    return ans;
}
