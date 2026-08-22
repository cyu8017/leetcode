// LeetCode 3372 - Maximize the Number of Target Nodes After Connecting Trees I
// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct { int* a; int n, cap; } Adj;
static void adj_push(Adj* g, int u, int v) {
    if (g[u].n == g[u].cap) { g[u].cap = g[u].cap ? g[u].cap * 2 : 4; g[u].a = (int*)realloc(g[u].a, g[u].cap * sizeof(int)); }
    g[u].a[g[u].n++] = v;
}
static int countWithin(Adj* g, int n, int start, int k) {
    if (k < 0) return 0;
    bool* vis = (bool*)calloc(n, 1);
    int* qu = (int*)malloc(n * sizeof(int));
    int* qd = (int*)malloc(n * sizeof(int));
    int qh = 0, qt = 0, cnt = 0;
    qu[qt] = start; qd[qt++] = 0; vis[start] = true;
    while (qh < qt) {
        int u = qu[qh], d = qd[qh++]; cnt++;
        if (d == k) continue;
        for (int i = 0; i < g[u].n; i++) {
            int v = g[u].a[i];
            if (!vis[v]) { vis[v] = true; qu[qt] = v; qd[qt++] = d + 1; }
        }
    }
    free(vis); free(qu); free(qd);
    return cnt;
}

int* maxTargetNodes(int** edges1, int edges1Size, int* edges1ColSize, int** edges2, int edges2Size, int* edges2ColSize, int k, int* returnSize) {
    (void)edges1ColSize; (void)edges2ColSize;
    int n = edges1Size + 1, m = edges2Size + 1;
    Adj* g1 = (Adj*)calloc(n, sizeof(Adj));
    Adj* g2 = (Adj*)calloc(m, sizeof(Adj));
    for (int i = 0; i < edges1Size; i++) { adj_push(g1, edges1[i][0], edges1[i][1]); adj_push(g1, edges1[i][1], edges1[i][0]); }
    for (int i = 0; i < edges2Size; i++) { adj_push(g2, edges2[i][0], edges2[i][1]); adj_push(g2, edges2[i][1], edges2[i][0]); }
    int best2 = 0;
    if (k > 0) for (int i = 0; i < m; i++) { int c = countWithin(g2, m, i, k - 1); if (c > best2) best2 = c; }
    int* ans = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) ans[i] = countWithin(g1, n, i, k) + best2;
    for (int i = 0; i < n; i++) free(g1[i].a); for (int i = 0; i < m; i++) free(g2[i].a);
    free(g1); free(g2);
    *returnSize = n;
    return ans;
}
