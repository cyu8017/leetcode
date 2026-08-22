// LeetCode 2144 - Minimum Cost of Buying Candies With Discount
// https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/

#include <stdlib.h>

static int cmpDesc(const void* a, const void* b) {
    return *(const int*)b - *(const int*)a;
}

int minimumCost(int* cost, int costSize) {
    qsort(cost, (size_t)costSize, sizeof(int), cmpDesc);
    int ans = 0;
    for (int i = 0; i < costSize; i++) if (i % 3 != 2) ans += cost[i];
    return ans;
}
