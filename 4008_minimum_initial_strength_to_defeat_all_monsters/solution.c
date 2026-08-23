// LeetCode 4008 - Minimum Initial Strength To Defeat All Monsters
// https://leetcode.com/problems/minimum-initial-strength-to-defeat-all-monsters/

#include <stdlib.h>
#include <stdint.h>
#include <string.h>

static int check4008(int64_t v, int* monsters, int n, int64_t* d) {
    int64_t bonus = 0;
    for (int i = 0; i < n; i++) {
        bonus += d[i];
        if (v + bonus < (int64_t)monsters[i]) return 0;
        v -= (int64_t)monsters[i];
        if (v < 0) v = 0;
    }
    return 1;
}

long long minInitialStrength(int* monsters, int monstersSize, int** boosts, int boostsSize, int* boostsColSize) {
    (void)boostsColSize;
    int n = monstersSize;
    int64_t* d = (int64_t*)calloc((size_t)(n + 1), sizeof(int64_t));
    for (int i = 0; i < boostsSize; i++) {
        d[boosts[i][0]] += (int64_t)boosts[i][2];
        d[boosts[i][1] + 1] -= (int64_t)boosts[i][2];
    }

    int64_t left = 0, right = 1000000000000000LL;
    while (left < right) {
        int64_t mid = (left + right) / 2;
        if (check4008(mid, monsters, n, d)) right = mid;
        else left = mid + 1;
    }
    free(d);
    return left;
}
