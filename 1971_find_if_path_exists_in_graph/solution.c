// LeetCode 1971 - Find if Path Exists in Graph
// https://leetcode.com/problems/find-if-path-exists-in-graph/

#include <stdlib.h>
#include <stdbool.h>

static int find(int* p, int x) {
    while (p[x] != x) {
        p[x] = p[p[x]];
        x = p[x];
    }
    return x;
}

bool validPath(int n, int** edges, int edgesSize, int* edgesColSize, int source, int destination) {
    (void)edgesColSize;
    int* parent = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) parent[i] = i;
    for (int i = 0; i < edgesSize; i++) {
        int a = find(parent, edges[i][0]);
        int b = find(parent, edges[i][1]);
        if (a != b) parent[a] = b;
    }
    bool ok = find(parent, source) == find(parent, destination);
    free(parent);
    return ok;
}
