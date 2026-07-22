// LeetCode 1648 - Sell Diminishing-Valued Colored Balls
// https://leetcode.com/problems/sell-diminishing-valued-colored-balls/

#include <stdlib.h>

#define MOD 1000000007LL

static int cmpDesc(const void* a, const void* b) {
    return *(const int*)b - *(const int*)a;
}

int maxProfit(int* inventory, int inventorySize, int orders) {
    qsort(inventory, (size_t)inventorySize, sizeof(int), cmpDesc);
    int* inv = (int*)malloc((size_t)(inventorySize + 1) * sizeof(int));
    for (int i = 0; i < inventorySize; i++) inv[i] = inventory[i];
    inv[inventorySize] = 0;
    long long ans = 0;
    for (int i = 0; i < inventorySize; i++) {
        long long width = i + 1;
        long long high = inv[i], low = inv[i + 1];
        long long balls = width * (high - low);
        long long take = orders < balls ? orders : balls;
        long long full = take / width;
        long long rem = take % width;
        long long bottom = high - full;
        ans += width * (high + bottom + 1) * full / 2 + rem * bottom;
        orders -= (int)take;
        if (orders == 0) break;
    }
    free(inv);
    return (int)(ans % MOD);
}
