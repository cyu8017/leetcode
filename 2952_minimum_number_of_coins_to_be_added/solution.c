// LeetCode 2952 - Minimum Number of Coins to be Added
// https://leetcode.com/problems/minimum-number-of-coins-to-be-added/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) { return (*(const int*)a) - (*(const int*)b); }

int minimumAddedCoins(int* coins, int coinsSize, int target) {
    qsort(coins, coinsSize, sizeof(int), cmp_int);
    int ans = 0;
    long long reach = 0;
    int i = 0;
    while (reach < target) {
        if (i < coinsSize && coins[i] <= reach + 1) {
            reach += coins[i];
            i++;
        } else {
            reach += reach + 1;
            ans++;
        }
    }
    return ans;
}
