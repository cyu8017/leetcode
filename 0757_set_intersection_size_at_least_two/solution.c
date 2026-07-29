// LeetCode 0757 - Set Intersection Size At Least Two
// https://leetcode.com/problems/set-intersection-size-at-least-two/

#include <stdlib.h>

static int cmpIv(const void* a, const void* b) {
    const int* x = *(const int* const*)a;
    const int* y = *(const int* const*)b;
    if (x[1] != y[1]) return x[1] - y[1];
    return x[0] - y[0];
}

int intersectionSizeTwo(int** intervals, int intervalsSize, int* intervalsColSize) {
    (void)intervalsColSize;
    qsort(intervals, (size_t)intervalsSize, sizeof(int*), cmpIv);
    int size = 0, first = -1, second = -1;
    for (int i = 0; i < intervalsSize; i++) {
        int left = intervals[i][0], right = intervals[i][1];
        if (left <= first) continue;
        if (left <= second) {
            size += 1;
            first = second;
            second = right;
        } else {
            size += 2;
            first = right - 1;
            second = right;
        }
    }
    return size;
}
