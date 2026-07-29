// LeetCode 0436 - Find Right Interval
// https://leetcode.com/problems/find-right-interval/

#include <stdlib.h>

typedef struct {
    int start;
    int index;
} StartIndex;

static int cmpStart(const void* a, const void* b) {
    const StartIndex* left = (const StartIndex*)a;
    const StartIndex* right = (const StartIndex*)b;
    return left->start - right->start;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findRightInterval(int** intervals, int intervalsSize, int* intervalsColSize, int* returnSize) {
    (void)intervalsColSize;
    StartIndex* indexed = (StartIndex*)malloc((size_t)intervalsSize * sizeof(StartIndex));
    for (int i = 0; i < intervalsSize; i++) {
        indexed[i].start = intervals[i][0];
        indexed[i].index = i;
    }
    qsort(indexed, (size_t)intervalsSize, sizeof(StartIndex), cmpStart);

    int* result = (int*)malloc((size_t)intervalsSize * sizeof(int));
    for (int i = 0; i < intervalsSize; i++) {
        int end = intervals[i][1];
        int low = 0;
        int high = intervalsSize;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (indexed[mid].start < end) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        result[i] = low == intervalsSize ? -1 : indexed[low].index;
    }

    free(indexed);
    *returnSize = intervalsSize;
    return result;
}
