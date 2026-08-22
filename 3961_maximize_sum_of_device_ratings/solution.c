// LeetCode 3961 - Maximize Sum Of Device Ratings
// https://leetcode.com/problems/maximize-sum-of-device-ratings/

#include <stdlib.h>
#include <limits.h>

static int cmpInt3961(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

long long maxRatings(int** units, int unitsSize, int* unitsColSize) {
    int n = unitsColSize[0];
    if (n == 1) {
        long long ans = 0;
        for (int i = 0; i < unitsSize; i++) ans += units[i][0];
        return ans;
    }
    long long ans = 0;
    int mn = INT_MAX, mn2 = INT_MAX;
    for (int i = 0; i < unitsSize; i++) {
        int* x = malloc((size_t)n * sizeof(int));
        for (int j = 0; j < n; j++) x[j] = units[i][j];
        qsort(x, (size_t)n, sizeof(int), cmpInt3961);
        ans += x[1];
        if (x[1] < mn2) mn2 = x[1];
        if (x[0] < mn) mn = x[0];
        free(x);
    }
    return ans - (mn2 - mn);
}
