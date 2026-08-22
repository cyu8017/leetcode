// LeetCode 0452 - Minimum Number of Arrows to Burst Balloons
// https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

#include <stdlib.h>

static int cmpPoints(const void* a, const void* b) {
    int* const* left = (int* const*)a;
    int* const* right = (int* const*)b;
    if ((*left)[1] < (*right)[1]) {
        return -1;
    }
    if ((*left)[1] > (*right)[1]) {
        return 1;
    }
    return 0;
}

int findMinArrowShots(int** points, int pointsSize, int* pointsColSize) {
    (void)pointsColSize;
    if (pointsSize == 0) {
        return 0;
    }
    qsort(points, (size_t)pointsSize, sizeof(int*), cmpPoints);
    int arrows = 1;
    int end = points[0][1];
    for (int i = 1; i < pointsSize; i++) {
        if (points[i][0] > end) {
            arrows++;
            end = points[i][1];
        }
    }
    return arrows;
}
