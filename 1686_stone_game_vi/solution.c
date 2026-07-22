// LeetCode 1686 - Stone Game VI
// https://leetcode.com/problems/stone-game-vi/

#include <stdlib.h>

typedef struct { int sum; int i; } Pair;

static int cmpPair(const void* a, const void* b) {
    return ((const Pair*)b)->sum - ((const Pair*)a)->sum;
}

int stoneGameVI(int* aliceValues, int aliceValuesSize, int* bobValues, int bobValuesSize) {
    (void)bobValuesSize;
    int n = aliceValuesSize;
    Pair* order = (Pair*)malloc((size_t)n * sizeof(Pair));
    for (int i = 0; i < n; i++) {
        order[i].sum = aliceValues[i] + bobValues[i];
        order[i].i = i;
    }
    qsort(order, (size_t)n, sizeof(Pair), cmpPair);
    int score = 0;
    for (int t = 0; t < n; t++) {
        int i = order[t].i;
        if (t % 2 == 0) score += aliceValues[i];
        else score -= bobValues[i];
    }
    free(order);
    return (score > 0) - (score < 0);
}
