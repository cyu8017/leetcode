// LeetCode 1561 - Maximum Number of Coins You Can Get
// https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int maxCoins(int* piles, int pilesSize) {
    qsort(piles, (size_t)pilesSize, sizeof(int), cmpInt);
    int ans = 0;
    for (int i = pilesSize / 3; i < pilesSize; i += 2) ans += piles[i];
    return ans;
}
