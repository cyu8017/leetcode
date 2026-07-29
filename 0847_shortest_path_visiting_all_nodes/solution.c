// LeetCode 0847 - Shortest Path Visiting All Nodes
// https://leetcode.com/problems/shortest-path-visiting-all-nodes/

#include <stdlib.h>
#include <stdbool.h>

typedef struct { int node, mask, dist; } QNode;

int shortestPathLength(int** graph, int graphSize, int* graphColSize) {
    int n = graphSize;
    int target = (1 << n) - 1;
    int states = n * (1 << n);
    QNode* q = (QNode*)malloc((size_t)states * sizeof(QNode));
    bool* seen = (bool*)calloc((size_t)states, sizeof(bool));
    int qh = 0, qt = 0;
    for (int i = 0; i < n; i++) {
        int mask = 1 << i;
        q[qt++] = (QNode){i, mask, 0};
        seen[i * (1 << n) + mask] = true;
    }
    while (qh < qt) {
        QNode cur = q[qh++];
        if (cur.mask == target) {
            free(q); free(seen);
            return cur.dist;
        }
        for (int i = 0; i < graphColSize[cur.node]; i++) {
            int nxt = graph[cur.node][i];
            int nmask = cur.mask | (1 << nxt);
            int sid = nxt * (1 << n) + nmask;
            if (!seen[sid]) {
                seen[sid] = true;
                q[qt++] = (QNode){nxt, nmask, cur.dist + 1};
            }
        }
    }
    free(q); free(seen);
    return -1;
}
