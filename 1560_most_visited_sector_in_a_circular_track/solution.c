// LeetCode 1560 - Most Visited Sector in a Circular Track
// https://leetcode.com/problems/most-visited-sector-in-a-circular-track/

#include <stdlib.h>

int* mostVisited(int n, int* rounds, int roundsSize, int* returnSize) {
    int start = rounds[0], end = rounds[roundsSize - 1];
    int* ans = (int*)malloc((size_t)n * sizeof(int));
    int sz = 0;
    if (start <= end) {
        for (int i = start; i <= end; i++) ans[sz++] = i;
    } else {
        for (int i = 1; i <= end; i++) ans[sz++] = i;
        for (int i = start; i <= n; i++) ans[sz++] = i;
    }
    *returnSize = sz;
    return ans;
}
