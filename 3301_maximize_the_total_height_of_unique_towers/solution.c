// LeetCode 3301 - Maximize the Total Height of Unique Towers
// https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/

#include <stdlib.h>

static int cmpDesc(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    return (y > x) - (y < x);
}

long long maximumTotalSum(int* maximumHeight, int maximumHeightSize) {
    qsort(maximumHeight, (size_t)maximumHeightSize, sizeof(int), cmpDesc);
    long long ans = 0;
    long long prev = 1000000000000000000LL;
    for (int i = 0; i < maximumHeightSize; i++) {
        long long cur = maximumHeight[i];
        if (cur >= prev) cur = prev - 1;
        if (cur <= 0) return -1;
        ans += cur;
        prev = cur;
    }
    return ans;
}
