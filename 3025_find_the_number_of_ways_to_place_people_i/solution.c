// LeetCode 3025 - Find the Number of Ways to Place People I
// https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/

#include <stdlib.h>
#include <limits.h>

static int cmp_pts(const void* a, const void* b) {
    int* const* pa = (int* const*)a;
    int* const* pb = (int* const*)b;
    if ((*pa)[0] != (*pb)[0]) return (*pa)[0] - (*pb)[0];
    return (*pb)[1] - (*pa)[1];
}

int numberOfPairs(int** points, int pointsSize, int* pointsColSize) {
    (void)pointsColSize;
    qsort(points, (size_t)pointsSize, sizeof(int*), cmp_pts);
    int ans = 0;
    for (int i = 0; i < pointsSize; i++) {
        int y1 = points[i][1];
        int maxY = INT_MIN;
        for (int j = i + 1; j < pointsSize; j++) {
            int y2 = points[j][1];
            if (maxY < y2 && y2 <= y1) { maxY = y2; ans++; }
        }
    }
    return ans;
}
