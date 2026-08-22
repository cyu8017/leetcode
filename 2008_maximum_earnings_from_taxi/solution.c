// LeetCode 2008 - Maximum Earnings From Taxi
// https://leetcode.com/problems/maximum-earnings-from-taxi/

#include <stdlib.h>

static int cmpRideEnd(const void* a, const void* b) {
    int* const* ra = (int* const*)a;
    int* const* rb = (int* const*)b;
    return (*ra)[1] - (*rb)[1];
}

long long maxTaxiEarnings(int n, int** rides, int ridesSize, int* ridesColSize) {
    (void)n; (void)ridesColSize;
    qsort(rides, (size_t)ridesSize, sizeof(int*), cmpRideEnd);
    int* ends = (int*)malloc((size_t)ridesSize * sizeof(int));
    for (int i = 0; i < ridesSize; i++) ends[i] = rides[i][1];
    long long* dp = (long long*)calloc((size_t)(ridesSize + 1), sizeof(long long));
    for (int i = 0; i < ridesSize; i++) {
        int start = rides[i][0], end = rides[i][1], tip = rides[i][2];
        long long earn = (long long)(end - start + tip);
        int lo = 0, hi = ridesSize;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (ends[mid] > start) hi = mid;
            else lo = mid + 1;
        }
        long long cand = earn + dp[lo];
        dp[i + 1] = dp[i];
        if (cand > dp[i + 1]) dp[i + 1] = cand;
    }
    long long ans = dp[ridesSize];
    free(ends); free(dp);
    return ans;
}
