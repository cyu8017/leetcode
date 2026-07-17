// LeetCode 1798 - Maximum Number of Consecutive Values You Can Make
// https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int getMaximumConsecutive(int* coins, int coinsSize) {
    qsort(coins, coinsSize, sizeof(int), cmpInt);
    long long reach = 0;
    for (int i = 0; i < coinsSize; i++) {
        if (coins[i] > reach + 1) break;
        reach += coins[i];
    }
    return (int)(reach + 1);
}
