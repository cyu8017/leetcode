// LeetCode 0473 - Matchsticks to Square
// https://leetcode.com/problems/matchsticks-to-square/

#include <stdbool.h>
#include <stdlib.h>

static int cmpDesc(const void* a, const void* b) {
    return *(const int*)b - *(const int*)a;
}

static bool dfs(int* matchsticks, int matchsticksSize, int index, int* sides, int side) {
    if (index == matchsticksSize) {
        return sides[0] == side && sides[1] == side && sides[2] == side && sides[3] == side;
    }
    int length = matchsticks[index];
    for (int sideIndex = 0; sideIndex < 4; sideIndex++) {
        if (sides[sideIndex] + length > side) {
            continue;
        }
        if (sideIndex > 0 && sides[sideIndex] == sides[sideIndex - 1]) {
            continue;
        }
        sides[sideIndex] += length;
        if (dfs(matchsticks, matchsticksSize, index + 1, sides, side)) {
            return true;
        }
        sides[sideIndex] -= length;
    }
    return false;
}

bool makesquare(int* matchsticks, int matchsticksSize) {
    if (matchsticksSize == 0) {
        return false;
    }
    int total = 0;
    for (int i = 0; i < matchsticksSize; i++) {
        total += matchsticks[i];
    }
    if (total % 4 != 0) {
        return false;
    }
    int side = total / 4;
    qsort(matchsticks, (size_t)matchsticksSize, sizeof(int), cmpDesc);
    int sides[4] = {0, 0, 0, 0};
    return dfs(matchsticks, matchsticksSize, 0, sides, side);
}
