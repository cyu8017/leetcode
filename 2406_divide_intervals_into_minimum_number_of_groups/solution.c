// LeetCode 2406 - Divide Intervals Into Minimum Number of Groups
// https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

#include <stdlib.h>

typedef struct { int t, d; } Ev;
static int cmpEv(const void* a, const void* b) {
    const Ev* pa = (const Ev*)a; const Ev* pb = (const Ev*)b;
    if (pa->t != pb->t) return pa->t - pb->t;
    return pa->d - pb->d;
}

int minGroups(int** intervals, int intervalsSize, int* intervalsColSize) {
    (void)intervalsColSize;
    Ev* events = (Ev*)malloc((size_t)intervalsSize * 2 * sizeof(Ev));
    for (int i = 0; i < intervalsSize; i++) {
        events[2*i] = (Ev){intervals[i][0], 1};
        events[2*i+1] = (Ev){intervals[i][1] + 1, -1};
    }
    qsort(events, (size_t)intervalsSize * 2, sizeof(Ev), cmpEv);
    int cur = 0, ans = 0;
    for (int i = 0; i < intervalsSize * 2; i++) {
        cur += events[i].d;
        if (cur > ans) ans = cur;
    }
    free(events);
    return ans;
}
