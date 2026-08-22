// LeetCode 3975 - Filter Occupied Intervals
// https://leetcode.com/problems/filter-occupied-intervals/

#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *returnColumnSizes array must be malloced, assume caller calls free().
 */
static int cmpStart(const void* a, const void* b) {
    int* x = *(int* const*)a;
    int* y = *(int* const*)b;
    if (x[0] < y[0]) return -1;
    if (x[0] > y[0]) return 1;
    return 0;
}

int** filterOccupiedIntervals(int** occupiedIntervals, int occupiedIntervalsSize, int* occupiedIntervalsColSize,
                              int freeStart, int freeEnd, int* returnSize, int** returnColumnSizes) {
    (void)occupiedIntervalsColSize;
    qsort(occupiedIntervals, (size_t)occupiedIntervalsSize, sizeof(int*), cmpStart);

    int* starts = (int*)malloc((size_t)occupiedIntervalsSize * sizeof(int));
    int* ends = (int*)malloc((size_t)occupiedIntervalsSize * sizeof(int));
    int busyCnt = 0;
    starts[0] = occupiedIntervals[0][0];
    ends[0] = occupiedIntervals[0][1];
    busyCnt = 1;

    for (int i = 1; i < occupiedIntervalsSize; i++) {
        int s = occupiedIntervals[i][0];
        int e = occupiedIntervals[i][1];
        if (ends[busyCnt - 1] + 1 < s) {
            starts[busyCnt] = s;
            ends[busyCnt] = e;
            busyCnt++;
        } else if (e > ends[busyCnt - 1]) {
            ends[busyCnt - 1] = e;
        }
    }

    int cap = busyCnt * 2;
    int** ans = (int**)malloc((size_t)cap * sizeof(int*));
    int* colSizes = (int*)malloc((size_t)cap * sizeof(int));
    int cnt = 0;

    for (int i = 0; i < busyCnt; i++) {
        int s = starts[i], e = ends[i];
        if (e < freeStart || s > freeEnd) {
            ans[cnt] = (int*)malloc(2 * sizeof(int));
            ans[cnt][0] = s;
            ans[cnt][1] = e;
            colSizes[cnt] = 2;
            cnt++;
        } else {
            if (s < freeStart) {
                ans[cnt] = (int*)malloc(2 * sizeof(int));
                ans[cnt][0] = s;
                ans[cnt][1] = freeStart - 1;
                colSizes[cnt] = 2;
                cnt++;
            }
            if (e > freeEnd) {
                ans[cnt] = (int*)malloc(2 * sizeof(int));
                ans[cnt][0] = freeEnd + 1;
                ans[cnt][1] = e;
                colSizes[cnt] = 2;
                cnt++;
            }
        }
    }

    free(starts);
    free(ends);
    *returnSize = cnt;
    *returnColumnSizes = colSizes;
    return ans;
}
