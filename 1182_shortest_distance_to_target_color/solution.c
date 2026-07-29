// LeetCode 1182 - Shortest Distance to Target Color
// https://leetcode.com/problems/shortest-distance-to-target-color/

#include <limits.h>
#include <stdlib.h>
#include <string.h>

static int lowerBound(int* arr, int size, int target) {
    int lo = 0, hi = size;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (arr[mid] < target) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}

int* shortestDistanceColor(int* colors, int colorsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int pos[4][10000];
    int counts[4] = {0, 0, 0, 0};
    for (int i = 0; i < colorsSize; i++) {
        int c = colors[i];
        pos[c][counts[c]++] = i;
    }
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    for (int q = 0; q < queriesSize; q++) {
        int i = queries[q][0];
        int c = queries[q][1];
        if (counts[c] == 0) {
            ans[q] = -1;
            continue;
        }
        int idx = lowerBound(pos[c], counts[c], i);
        int best = INT_MAX;
        if (idx < counts[c]) {
            int d = pos[c][idx] - i;
            if (d < best) best = d;
        }
        if (idx > 0) {
            int d = i - pos[c][idx - 1];
            if (d < best) best = d;
        }
        ans[q] = best;
    }
    *returnSize = queriesSize;
    return ans;
}
