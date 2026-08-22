// LeetCode 3281 - Maximize Score of Numbers in Ranges
// https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

#include <stdlib.h>

static int cmpAsc(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    return (x > y) - (x < y);
}

static int ok3281(int* start, int n, int d, int mid) {
    long long prev = start[0];
    for (int i = 1; i < n; i++) {
        long long need = prev + mid;
        long long cur = start[i];
        if (need > cur + d) return 0;
        prev = need > cur ? need : cur;
    }
    return 1;
}

int maxPossibleScore(int* start, int startSize, int d) {
    qsort(start, (size_t)startSize, sizeof(int), cmpAsc);
    int n = startSize;
    int lo = 0, hi = start[n - 1] + d - start[0] + 1;
    while (lo < hi) {
        int mid = (lo + hi + 1) / 2;
        if (ok3281(start, n, d, mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
}
