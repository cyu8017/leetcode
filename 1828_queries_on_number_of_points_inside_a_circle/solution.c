// LeetCode 1828 - Queries on Number of Points Inside a Circle
// https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countPoints(int** points, int pointsSize, int* pointsColSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)pointsColSize;
    (void)queriesColSize;
    int* result = (int*)malloc((size_t)queriesSize * sizeof(int));
    for (int q = 0; q < queriesSize; q++) {
        int xq = queries[q][0], yq = queries[q][1], r = queries[q][2];
        long long radiusSq = (long long)r * r;
        int count = 0;
        for (int i = 0; i < pointsSize; i++) {
            long long dx = points[i][0] - xq;
            long long dy = points[i][1] - yq;
            if (dx * dx + dy * dy <= radiusSq) count++;
        }
        result[q] = count;
    }
    *returnSize = queriesSize;
    return result;
}
