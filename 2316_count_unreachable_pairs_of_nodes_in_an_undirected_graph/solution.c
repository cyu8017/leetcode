// LeetCode 2316 - Count Unreachable Pairs of Nodes in an Undirected Graph
// https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

long long countPairs(int n, int** edges, int edgesSize, int* edgesColSize) {
    (void)edgesColSize;
    int* head = (int*)malloc((size_t)n * sizeof(int));
    memset(head, -1, (size_t)n * sizeof(int));
    int* to = (int*)malloc((size_t)edgesSize * 2 * sizeof(int));
    int* next = (int*)malloc((size_t)edgesSize * 2 * sizeof(int));
    int ec = 0;
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1];
        to[ec] = v; next[ec] = head[u]; head[u] = ec++;
        to[ec] = u; next[ec] = head[v]; head[v] = ec++;
    }
    bool* vis = (bool*)calloc((size_t)n, sizeof(bool));
    int* stack = (int*)malloc((size_t)n * sizeof(int));
    long long ans = 0, seen = 0;
    for (int i = 0; i < n; i++) {
        if (vis[i]) continue;
        int top = 0;
        stack[top++] = i;
        vis[i] = true;
        long long sz = 0;
        while (top) {
            int u = stack[--top];
            sz++;
            for (int e = head[u]; e != -1; e = next[e]) {
                int v = to[e];
                if (!vis[v]) { vis[v] = true; stack[top++] = v; }
            }
        }
        ans += sz * seen;
        seen += sz;
    }
    free(head); free(to); free(next); free(vis); free(stack);
    return ans;
}
