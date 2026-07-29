// LeetCode 1129 - Shortest Path with Alternating Colors
// https://leetcode.com/problems/shortest-path-with-alternating-colors/

#include <stdlib.h>
#include <string.h>

int* shortestAlternatingPaths(int n, int** redEdges, int redEdgesSize, int* redEdgesColSize, int** blueEdges, int blueEdgesSize, int* blueEdgesColSize, int* returnSize) {
    (void)redEdgesColSize; (void)blueEdgesColSize;
    int* redHead = (int*)malloc((size_t)n * sizeof(int));
    int* blueHead = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) { redHead[i] = -1; blueHead[i] = -1; }
    int* redTo = (int*)malloc((size_t)(redEdgesSize + 1) * sizeof(int));
    int* redNext = (int*)malloc((size_t)(redEdgesSize + 1) * sizeof(int));
    int* blueTo = (int*)malloc((size_t)(blueEdgesSize + 1) * sizeof(int));
    int* blueNext = (int*)malloc((size_t)(blueEdgesSize + 1) * sizeof(int));
    for (int i = 0; i < redEdgesSize; i++) {
        int u = redEdges[i][0], v = redEdges[i][1];
        redTo[i] = v; redNext[i] = redHead[u]; redHead[u] = i;
    }
    for (int i = 0; i < blueEdgesSize; i++) {
        int u = blueEdges[i][0], v = blueEdges[i][1];
        blueTo[i] = v; blueNext[i] = blueHead[u]; blueHead[u] = i;
    }
    int* ans = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) ans[i] = -1;
    char* seen = (char*)calloc((size_t)n * 2, 1);
    int* qn = (int*)malloc((size_t)n * 2 * sizeof(int));
    int* qc = (int*)malloc((size_t)n * 2 * sizeof(int));
    int* qd = (int*)malloc((size_t)n * 2 * sizeof(int));
    int qs = 0, qe = 0;
    qn[qe] = 0; qc[qe] = 0; qd[qe] = 0; qe++; seen[0] = 1;
    qn[qe] = 0; qc[qe] = 1; qd[qe] = 0; qe++; seen[1] = 1;
    while (qs < qe) {
        int node = qn[qs], color = qc[qs], dist = qd[qs]; qs++;
        if (ans[node] == -1) ans[node] = dist;
        int nextColor = 1 - color;
        int* head = color == 0 ? redHead : blueHead;
        int* to = color == 0 ? redTo : blueTo;
        int* next = color == 0 ? redNext : blueNext;
        for (int e = head[node]; e != -1; e = next[e]) {
            int nxt = to[e];
            int state = nxt * 2 + nextColor;
            if (!seen[state]) {
                seen[state] = 1;
                qn[qe] = nxt; qc[qe] = nextColor; qd[qe] = dist + 1; qe++;
            }
        }
    }
    free(redHead); free(blueHead); free(redTo); free(redNext); free(blueTo); free(blueNext);
    free(seen); free(qn); free(qc); free(qd);
    *returnSize = n;
    return ans;
}
