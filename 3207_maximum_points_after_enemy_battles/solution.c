// LeetCode 3207 - Maximum Points After Enemy Battles
// https://leetcode.com/problems/maximum-points-after-enemy-battles/

#include <stdlib.h>

static int cmp3207(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

long long maximumPoints(int* enemyEnergies, int enemyEnergiesSize, int currentEnergy) {
    qsort(enemyEnergies, enemyEnergiesSize, sizeof(int), cmp3207);
    if (currentEnergy < enemyEnergies[0]) return 0;
    long long ans = 0;
    long long cur = currentEnergy;
    for (int i = enemyEnergiesSize - 1; i >= 0; i--) {
        ans += cur / enemyEnergies[0];
        cur %= enemyEnergies[0];
        cur += enemyEnergies[i];
    }
    return ans;
}
