// LeetCode 3323 - Minimize Connected Groups by Inserting Interval
// https://leetcode.com/problems/minimize-connected-groups-by-inserting-interval/

#include <stdlib.h>

static int cmpInt0(const void* a, const void* b) {
    int* const* x = (int* const*)a;
    int* const* y = (int* const*)b;
    return ((*x)[0] > (*y)[0]) - ((*x)[0] < (*y)[0]);
}

int minConnectedGroups(int** intervals, int intervalsSize, int* intervalsColSize, int k) {
    (void)intervalsColSize;
    qsort(intervals, (size_t)intervalsSize, sizeof(int*), cmpInt0);
    int** merged = (int**)malloc((size_t)intervalsSize * sizeof(int*));
    int mn = 0;
    for (int i = 0; i < intervalsSize; i++) {
        if (mn == 0 || intervals[i][0] > merged[mn - 1][1]) {
            merged[mn] = (int*)malloc(2 * sizeof(int));
            merged[mn][0] = intervals[i][0];
            merged[mn][1] = intervals[i][1];
            mn++;
        } else if (intervals[i][1] > merged[mn - 1][1]) {
            merged[mn - 1][1] = intervals[i][1];
        }
    }
    int ans = mn;
    for (int i = 0; i < mn; i++) {
        int end = merged[i][1] + k;
        int j = i;
        while (j < mn && merged[j][0] <= end) j++;
        int groups = i + 1 + (mn - j);
        if (groups < ans) ans = groups;
    }
    for (int i = 0; i < mn; i++) free(merged[i]);
    free(merged);
    return ans;
}
