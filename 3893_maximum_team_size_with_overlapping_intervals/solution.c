// LeetCode 3893 - Maximum Team Size With Overlapping Intervals
// https://leetcode.com/problems/maximum-team-size-with-overlapping-intervals/

#include <stdlib.h>
#include <string.h>

static int cmpInt3893(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

static int lowerBound3893(int* a, int n, int x) {
    /* first index with a[k] > x-1 i.e. a[k] >= x  for endTime > l-1 */
    int lo = 0, hi = n;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (a[mid] > x) hi = mid; /* wait: Search for endTime[k] > l-1 means first > (l-1) */
        else lo = mid + 1;
    }
    return lo;
}

int maximumTeamSize(int* startTime, int startTimeSize, int* endTime, int endTimeSize) {
    int n = startTimeSize;
    int* intervalsL = malloc((size_t)n * sizeof(int));
    int* intervalsR = malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) { intervalsL[i] = startTime[i]; intervalsR[i] = endTime[i]; }
    int* st = malloc((size_t)n * sizeof(int));
    int* en = malloc((size_t)n * sizeof(int));
    memcpy(st, startTime, (size_t)n * sizeof(int));
    memcpy(en, endTime, (size_t)n * sizeof(int));
    qsort(st, (size_t)n, sizeof(int), cmpInt3893);
    qsort(en, (size_t)n, sizeof(int), cmpInt3893);
    int ans = 0;
    for (int t = 0; t < n; t++) {
        int l = intervalsL[t], r = intervalsR[t];
        /* i := first endTime[k] > l-1 */
        int lo = 0, hi = n;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (en[mid] > l - 1) hi = mid;
            else lo = mid + 1;
        }
        int i = lo;
        lo = 0; hi = n;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (st[mid] > r) hi = mid;
            else lo = mid + 1;
        }
        int j = lo;
        if (j - i > ans) ans = j - i;
    }
    free(intervalsL); free(intervalsR); free(st); free(en);
    return ans;
}
