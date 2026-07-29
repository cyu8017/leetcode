// LeetCode 1288 - Remove Covered Intervals
// https://leetcode.com/problems/remove-covered-intervals/

#include <stdlib.h>

static int cmp_interval(const void* a, const void* b) {
    const int* ia = *(const int* const*)a;
    const int* ib = *(const int* const*)b;
    if (ia[0] != ib[0]) return ia[0] - ib[0];
    return ib[1] - ia[1];
}

int removeCoveredIntervals(int** intervals, int intervalsSize, int* intervalsColSize) {
    (void)intervalsColSize;
    qsort(intervals, (size_t)intervalsSize, sizeof(int*), cmp_interval);
    int answer = 0, farthest = -1;
    for (int i = 0; i < intervalsSize; i++) {
        if (intervals[i][1] > farthest) {
            answer++;
            farthest = intervals[i][1];
        }
    }
    return answer;
}
