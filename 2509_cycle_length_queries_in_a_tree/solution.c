// LeetCode 2509 - Cycle Length Queries in a Tree
// https://leetcode.com/problems/cycle-length-queries-in-a-tree/

#include <stdlib.h>

int* cycleLengthQueries(int n, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)n; (void)queriesColSize;
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; i++) {
        int a = queries[i][0], b = queries[i][1];
        int steps = 0;
        while (a != b) {
            if (a > b) a /= 2;
            else b /= 2;
            steps++;
        }
        ans[i] = steps + 1;
    }
    *returnSize = queriesSize;
    return ans;
}
