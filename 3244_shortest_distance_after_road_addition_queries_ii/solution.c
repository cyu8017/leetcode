// LeetCode 3244 - Shortest Distance After Road Addition Queries II
// https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/

#include <stdlib.h>

int* shortestDistanceAfterQueries(int n, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int* nxt = (int*)malloc((size_t)(n - 1) * sizeof(int));
    for (int i = 0; i < n - 1; i++) nxt[i] = i + 1;
    int cnt = n - 1;
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    for (int qi = 0; qi < queriesSize; qi++) {
        int u = queries[qi][0], v = queries[qi][1];
        if (nxt[u] > 0 && nxt[u] < v) {
            int i = nxt[u];
            while (i < v) {
                cnt--;
                int ni = nxt[i];
                nxt[i] = 0;
                i = ni;
            }
            nxt[u] = v;
        }
        ans[qi] = cnt;
    }
    free(nxt);
    *returnSize = queriesSize;
    return ans;
}
