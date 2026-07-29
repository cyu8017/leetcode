// LeetCode 0759 - Employee Free Time
#include <stdlib.h>

struct Interval {
    int start;
    int end;
};

static int cmpIv(const void* a, const void* b) {
    const struct Interval* x = (const struct Interval*)a;
    const struct Interval* y = (const struct Interval*)b;
    return x->start - y->start;
}

struct Interval* employeeFreeTime(struct Interval** schedule, int scheduleSize, int* scheduleColSize, int* returnSize) {
    int total = 0;
    for (int i = 0; i < scheduleSize; i++) total += scheduleColSize[i];
    struct Interval* intervals = (struct Interval*)malloc((size_t)total * sizeof(struct Interval));
    int n = 0;
    for (int i = 0; i < scheduleSize; i++)
        for (int j = 0; j < scheduleColSize[i]; j++)
            intervals[n++] = schedule[i][j];
    qsort(intervals, (size_t)n, sizeof(struct Interval), cmpIv);
    struct Interval* merged = (struct Interval*)malloc((size_t)n * sizeof(struct Interval));
    int m = 0;
    for (int i = 0; i < n; i++) {
        if (m == 0 || merged[m - 1].end < intervals[i].start) merged[m++] = intervals[i];
        else if (intervals[i].end > merged[m - 1].end) merged[m - 1].end = intervals[i].end;
    }
    struct Interval* result = (struct Interval*)malloc((size_t)m * sizeof(struct Interval));
    int r = 0;
    for (int i = 1; i < m; i++) {
        result[r].start = merged[i - 1].end;
        result[r].end = merged[i].start;
        r++;
    }
    free(intervals); free(merged);
    *returnSize = r;
    return result;
}
