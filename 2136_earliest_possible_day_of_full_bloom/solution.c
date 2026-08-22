// LeetCode 2136 - Earliest Possible Day of Full Bloom
// https://leetcode.com/problems/earliest-possible-day-of-full-bloom/

#include <stdlib.h>

typedef struct { int plant; int grow; } Flower;

static int cmpGrowDesc(const void* a, const void* b) {
    return ((const Flower*)b)->grow - ((const Flower*)a)->grow;
}

int earliestFullBloom(int* plantTime, int plantTimeSize, int* growTime, int growTimeSize) {
    (void)growTimeSize;
    int n = plantTimeSize;
    Flower* f = (Flower*)malloc((size_t)n * sizeof(Flower));
    for (int i = 0; i < n; i++) { f[i].plant = plantTime[i]; f[i].grow = growTime[i]; }
    qsort(f, (size_t)n, sizeof(Flower), cmpGrowDesc);
    int day = 0, ans = 0;
    for (int i = 0; i < n; i++) {
        day += f[i].plant;
        if (day + f[i].grow > ans) ans = day + f[i].grow;
    }
    free(f);
    return ans;
}
