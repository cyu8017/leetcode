// LeetCode 0056 - Merge Intervals
// https://leetcode.com/problems/merge-intervals/

#include <stdlib.h>

typedef struct {
    int start;
    int end;
} Interval;

static int cmpInterval(const void* a, const void* b) {
    return ((const Interval*)a)->start - ((const Interval*)b)->start;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *returnColumnSizes array must be malloced by caller.
 */
int** merge(int** intervals, int intervalsSize, int* intervalsColSize, int* returnSize, int** returnColumnSizes) {
    Interval* sorted = (Interval*)malloc((size_t)intervalsSize * sizeof(Interval));
    for (int i = 0; i < intervalsSize; i++) {
        sorted[i].start = intervals[i][0];
        sorted[i].end = intervals[i][1];
    }
    qsort(sorted, (size_t)intervalsSize, sizeof(Interval), cmpInterval);

    int capacity = intervalsSize;
    int** result = (int**)malloc((size_t)capacity * sizeof(int*));
    int* colSizes = (int*)malloc((size_t)capacity * sizeof(int));
    int count = 0;

    result[count] = (int*)malloc(2 * sizeof(int));
    result[count][0] = sorted[0].start;
    result[count][1] = sorted[0].end;
    colSizes[count] = 2;
    count++;

    for (int i = 1; i < intervalsSize; i++) {
        int* last = result[count - 1];
        if (sorted[i].start <= last[1]) {
            if (sorted[i].end > last[1]) {
                last[1] = sorted[i].end;
            }
        } else {
            result[count] = (int*)malloc(2 * sizeof(int));
            result[count][0] = sorted[i].start;
            result[count][1] = sorted[i].end;
            colSizes[count] = 2;
            count++;
        }
    }

    free(sorted);
    *returnSize = count;
    *returnColumnSizes = (int*)realloc(colSizes, (size_t)count * sizeof(int));
    result = (int**)realloc(result, (size_t)count * sizeof(int*));
    return result;
}
