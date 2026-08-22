// LeetCode 2054 - Two Best Non-Overlapping Events
// https://leetcode.com/problems/two-best-non-overlapping-events/

#include <stdlib.h>

static int cmpEvStart(const void* a, const void* b) {
    int* const* ea = (int* const*)a;
    int* const* eb = (int* const*)b;
    return (*ea)[0] - (*eb)[0];
}

int maxTwoEvents(int** events, int eventsSize, int* eventsColSize) {
    (void)eventsColSize;
    qsort(events, (size_t)eventsSize, sizeof(int*), cmpEvStart);
    int n = eventsSize;
    int* suffix = (int*)calloc((size_t)n + 1, sizeof(int));
    for (int i = n - 1; i >= 0; i--) {
        suffix[i] = suffix[i + 1];
        if (events[i][2] > suffix[i]) suffix[i] = events[i][2];
    }
    int ans = 0;
    for (int i = 0; i < n; i++) {
        if (events[i][2] > ans) ans = events[i][2];
        int lo = i + 1, hi = n;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (events[mid][0] > events[i][1]) hi = mid;
            else lo = mid + 1;
        }
        if (lo < n && events[i][2] + suffix[lo] > ans) ans = events[i][2] + suffix[lo];
    }
    free(suffix);
    return ans;
}
