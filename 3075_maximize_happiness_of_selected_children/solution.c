// LeetCode 3075 - Maximize Happiness of Selected Children
// https://leetcode.com/problems/maximize-happiness-of-selected-children/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) {
    return (*(const int*)a) - (*(const int*)b);
}

long long maximumHappinessSum(int* happiness, int happinessSize, int k) {
    qsort(happiness, (size_t)happinessSize, sizeof(int), cmp_int);
    long long ans = 0;
    for (int i = 0; i < k; i++) {
        long long x = (long long)happiness[happinessSize - i - 1] - i;
        if (x > 0) ans += x;
    }
    return ans;
}
