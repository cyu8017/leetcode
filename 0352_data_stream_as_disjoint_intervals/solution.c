// LeetCode 0352 - Data Stream as Disjoint Intervals
// https://leetcode.com/problems/data-stream-as-disjoint-intervals/

#include <stdlib.h>

typedef struct {
    int start;
    int end;
} Interval;

typedef struct {
    Interval* intervals;
    int count;
    int capacity;
} SummaryRanges;

SummaryRanges* summaryRangesCreate() {
    SummaryRanges* obj = (SummaryRanges*)calloc(1, sizeof(SummaryRanges));
    return obj;
}

void summaryRangesAddNum(SummaryRanges* obj, int value) {
    Interval newInterval = {value, value};
    Interval* merged = (Interval*)calloc((size_t)(obj->count + 1), sizeof(Interval));
    int mergedCount = 0;
    int inserted = 0;

    for (int index = 0; index < obj->count; index++) {
        Interval interval = obj->intervals[index];
        if (interval.end < value - 1) {
            merged[mergedCount++] = interval;
        } else if (interval.start > value + 1) {
            if (!inserted) {
                merged[mergedCount++] = newInterval;
                inserted = 1;
            }
            merged[mergedCount++] = interval;
        } else {
            if (interval.start < newInterval.start) {
                newInterval.start = interval.start;
            }
            if (interval.end > newInterval.end) {
                newInterval.end = interval.end;
            }
        }
    }

    if (!inserted) {
        merged[mergedCount++] = newInterval;
    }

    free(obj->intervals);
    obj->intervals = merged;
    obj->count = mergedCount;
    obj->capacity = mergedCount;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *returnColumnSizes array must be malloced, assume caller calls free().
 */
int** summaryRangesGetIntervals(SummaryRanges* obj, int* returnSize, int** returnColumnSizes) {
    *returnSize = obj->count;
    if (obj->count == 0) {
        *returnColumnSizes = NULL;
        return NULL;
    }

    int** result = (int**)malloc((size_t)obj->count * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)obj->count * sizeof(int));

    for (int index = 0; index < obj->count; index++) {
        result[index] = (int*)malloc(2 * sizeof(int));
        result[index][0] = obj->intervals[index].start;
        result[index][1] = obj->intervals[index].end;
        (*returnColumnSizes)[index] = 2;
    }

    return result;
}

void summaryRangesFree(SummaryRanges* obj) {
    free(obj->intervals);
    free(obj);
}
