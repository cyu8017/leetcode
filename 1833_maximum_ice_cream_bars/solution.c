// LeetCode 1833 - Maximum Ice Cream Bars
// https://leetcode.com/problems/maximum-ice-cream-bars/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    return (x > y) - (x < y);
}

int maxIceCream(int* costs, int costsSize, int coins) {
    qsort(costs, (size_t)costsSize, sizeof(int), cmpInt);
    int count = 0;
    for (int i = 0; i < costsSize; i++) {
        if (coins < costs[i]) break;
        coins -= costs[i];
        count++;
    }
    return count;
}
