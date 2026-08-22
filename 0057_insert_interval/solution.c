// LeetCode 0057 - Insert Interval
// https://leetcode.com/problems/insert-interval/

#include <stdlib.h>

static void appendInterval(int*** result, int** colSizes, int* count, int* capacity, int start, int end) {
    if (*count >= *capacity) {
        *capacity = *capacity == 0 ? 8 : *capacity * 2;
        *result = (int**)realloc(*result, (size_t)(*capacity) * sizeof(int*));
        *colSizes = (int*)realloc(*colSizes, (size_t)(*capacity) * sizeof(int));
    }
    (*result)[*count] = (int*)malloc(2 * sizeof(int));
    (*result)[*count][0] = start;
    (*result)[*count][1] = end;
    (*colSizes)[*count] = 2;
    (*count)++;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *returnColumnSizes array must be malloced by caller.
 */
int** insert(int** intervals, int intervalsSize, int* intervalsColSize, int* newInterval, int newIntervalSize, int* returnSize, int** returnColumnSizes) {
    (void)intervalsColSize;
    (void)newIntervalSize;

    int capacity = intervalsSize + 1;
    int** result = (int**)malloc((size_t)capacity * sizeof(int*));
    int* colSizes = (int*)malloc((size_t)capacity * sizeof(int));
    int count = 0;
    int i = 0;
    int start = newInterval[0];
    int end = newInterval[1];

    while (i < intervalsSize && intervals[i][1] < start) {
        appendInterval(&result, &colSizes, &count, &capacity, intervals[i][0], intervals[i][1]);
        i++;
    }

    while (i < intervalsSize && intervals[i][0] <= end) {
        if (intervals[i][0] < start) {
            start = intervals[i][0];
        }
        if (intervals[i][1] > end) {
            end = intervals[i][1];
        }
        i++;
    }

    appendInterval(&result, &colSizes, &count, &capacity, start, end);

    while (i < intervalsSize) {
        appendInterval(&result, &colSizes, &count, &capacity, intervals[i][0], intervals[i][1]);
        i++;
    }

    *returnSize = count;
    *returnColumnSizes = (int*)realloc(colSizes, (size_t)count * sizeof(int));
    result = (int**)realloc(result, (size_t)count * sizeof(int*));
    return result;
}
