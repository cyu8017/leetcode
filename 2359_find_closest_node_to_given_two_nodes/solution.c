// LeetCode 2359 - Find Closest Node to Given Two Nodes
// https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

#include <stdlib.h>

static void distFrom(int* edges, int n, int start, int* d) {
    for (int i = 0; i < n; i++) d[i] = -1;
    int cur = start, step = 0;
    while (cur != -1 && d[cur] == -1) {
        d[cur] = step;
        cur = edges[cur];
        step++;
    }
}

int closestMeetingNode(int* edges, int edgesSize, int node1, int node2) {
    int n = edgesSize;
    int* d1 = (int*)malloc((size_t)n * sizeof(int));
    int* d2 = (int*)malloc((size_t)n * sizeof(int));
    distFrom(edges, n, node1, d1);
    distFrom(edges, n, node2, d2);
    int ans = -1, best = 1 << 30;
    for (int i = 0; i < n; i++) {
        if (d1[i] == -1 || d2[i] == -1) continue;
        int mx = d1[i] > d2[i] ? d1[i] : d2[i];
        if (mx < best) { best = mx; ans = i; }
    }
    free(d1); free(d2);
    return ans;
}
