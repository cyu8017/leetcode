// LeetCode 2603 - Collect Coins in a Tree
// https://leetcode.com/problems/collect-coins-in-a-tree/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int collectTheCoins(int* coins, int coinsSize, int** edges, int edgesSize, int* edgesColSize) {
    (void)edgesColSize;
    int n = coinsSize;
    int* head = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) head[i] = -1;
    int* to = (int*)malloc((size_t)(2 * edgesSize) * sizeof(int));
    int* next = (int*)malloc((size_t)(2 * edgesSize) * sizeof(int));
    int* alive = (int*)malloc((size_t)(2 * edgesSize) * sizeof(int));
    int ec = 0;
    #define ADD(u,v) do { to[ec]=v; next[ec]=head[u]; alive[ec]=1; head[u]=ec++; } while(0)
    for (int i = 0; i < edgesSize; i++) {
        ADD(edges[i][0], edges[i][1]);
        ADD(edges[i][1], edges[i][0]);
    }
    int* deg = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < n; i++) {
        for (int e = head[i]; e != -1; e = next[e]) if (alive[e]) deg[i]++;
    }
    int* q = (int*)malloc((size_t)n * sizeof(int));
    int qh = 0, qt = 0;
    bool* removed = (bool*)calloc((size_t)n, sizeof(bool));
    for (int i = 0; i < n; i++) {
        if (deg[i] == 1 && coins[i] == 0) { q[qt++] = i; }
    }
    while (qh < qt) {
        int u = q[qh++];
        if (removed[u]) continue;
        removed[u] = true;
        for (int e = head[u]; e != -1; e = next[e]) {
            if (!alive[e]) continue;
            int v = to[e];
            alive[e] = 0;
            alive[e ^ 1] = 0;
            deg[v]--;
            deg[u]--;
            if (!removed[v] && deg[v] == 1 && coins[v] == 0) q[qt++] = v;
        }
    }
    for (int round = 0; round < 2; round++) {
        int* leaves = (int*)malloc((size_t)n * sizeof(int));
        int lc = 0;
        for (int i = 0; i < n; i++) if (!removed[i] && deg[i] == 1) leaves[lc++] = i;
        for (int i = 0; i < lc; i++) {
            int u = leaves[i];
            if (removed[u]) continue;
            removed[u] = true;
            for (int e = head[u]; e != -1; e = next[e]) {
                if (!alive[e]) continue;
                int v = to[e];
                alive[e] = 0; alive[e ^ 1] = 0;
                deg[v]--; deg[u]--;
            }
        }
        free(leaves);
    }
    int remain = 0;
    for (int i = 0; i < n; i++) {
        if (removed[i]) continue;
        for (int e = head[i]; e != -1; e = next[e]) if (alive[e]) remain++;
    }
    free(head); free(to); free(next); free(alive); free(deg); free(q); free(removed);
    return remain;
}
