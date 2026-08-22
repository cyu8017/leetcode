// LeetCode 2790 - Maximum Number of Groups With Increasing Length
// https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int maxIncreasingGroups(int* usageLimits, int usageLimitsSize) {
    qsort(usageLimits, usageLimitsSize, sizeof(int), cmp_int);
    int ans = 0;
    long long sum = 0;
    for (int i = 0; i < usageLimitsSize; i++) {
        sum += usageLimits[i];
        long long need = (long long)(ans + 1) * (ans + 2) / 2;
        if (sum >= need) ans++;
    }
    return ans;
}
