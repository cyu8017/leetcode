// LeetCode 0435 - Non-overlapping Intervals
// https://leetcode.com/problems/non-overlapping-intervals/

#include <stdlib.h>

static int cmpInterval(const void* a, const void* b) {
    int* const* left = (int* const*)a;
    int* const* right = (int* const*)b;
    return (*left)[1] - (*right)[1];
}

int eraseOverlapIntervals(int** intervals, int intervalsSize, int* intervalsColSize) {
    (void)intervalsColSize;
    if (intervalsSize == 0) {
        return 0;
    }
    qsort(intervals, (size_t)intervalsSize, sizeof(int*), cmpInterval);
    int removed = 0;
    int end = intervals[0][1];
    for (int i = 1; i < intervalsSize; i++) {
        if (intervals[i][0] < end) {
            removed++;
        } else {
            end = intervals[i][1];
        }
    }
    return removed;
}
