// LeetCode 1751 - Maximum Number of Events That Can Be Attended II
// https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/

#include <stdlib.h>

static int compareEvents(const void* a, const void* b) {
    const int* ea = *(const int* const*) a;
    const int* eb = *(const int* const*) b;
    if (ea[0] != eb[0]) return ea[0] < eb[0] ? -1 : 1;
    if (ea[1] != eb[1]) return ea[1] < eb[1] ? -1 : 1;
    if (ea[2] != eb[2]) return ea[2] < eb[2] ? -1 : 1;
    return 0;
}

static int upperBound(const int* starts, int n, int target) {
    int lo = 0;
    int hi = n;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (starts[mid] <= target) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    return lo;
}

int maxValue(int** events, int eventsSize, int* eventsColSize, int k) {
    int n = eventsSize;
    qsort(events, n, sizeof(int*), compareEvents);

    int* starts = (int*) malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        starts[i] = events[i][0];
    }

    int* dp = (int*) calloc((size_t)(k + 1) * (n + 1), sizeof(int));
    for (int i = n - 1; i >= 0; i--) {
        int j = upperBound(starts, n, events[i][1]);
        for (int remain = 1; remain <= k; remain++) {
            int skip = dp[remain * (n + 1) + i + 1];
            int take = events[i][2] + dp[(remain - 1) * (n + 1) + j];
            dp[remain * (n + 1) + i] = skip > take ? skip : take;
        }
    }

    int answer = dp[k * (n + 1)];
    free(starts);
    free(dp);
    return answer;
}
