// LeetCode 3373 - Maximize the Number of Target Nodes After Connecting Trees II
// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/

#include <stdlib.h>
#include <string.h>

typedef struct { int* a; int n, cap; } Adj;
static void adj_push(Adj* g, int u, int v) {
    if (g[u].n == g[u].cap) { g[u].cap = g[u].cap ? g[u].cap * 2 : 4; g[u].a = (int*)realloc(g[u].a, g[u].cap * sizeof(int)); }
    g[u].a[g[u].n++] = v;
}
static void bipartite(Adj* g, int n, int* color, int* cnt) {
    for (int i = 0; i < n; i++) color[i] = -1;
    int* q = (int*)malloc(n * sizeof(int)); int qh = 0, qt = 0;
    q[qt++] = 0; color[0] = 0; cnt[0] = 1; cnt[1] = 0;
    while (qh < qt) {
        int u = q[qh++];
        for (int i = 0; i < g[u].n; i++) {
            int v = g[u].a[i];
            if (color[v] == -1) { color[v] = color[u] ^ 1; cnt[color[v]]++; q[qt++] = v; }
        }
    }
    free(q);
}

int* maxTargetNodes(int** edges1, int edges1Size, int* edges1ColSize, int** edges2, int edges2Size, int* edges2ColSize, int* returnSize) {
    (void)edges1ColSize; (void)edges2ColSize;
    int n = edges1Size + 1, m = edges2Size + 1;
    Adj* g1 = (Adj*)calloc(n, sizeof(Adj)); Adj* g2 = (Adj*)calloc(m, sizeof(Adj));
    for (int i = 0; i < edges1Size; i++) { adj_push(g1, edges1[i][0], edges1[i][1]); adj_push(g1, edges1[i][1], edges1[i][0]); }
    for (int i = 0; i < edges2Size; i++) { adj_push(g2, edges2[i][0], edges2[i][1]); adj_push(g2, edges2[i][1], edges2[i][0]); }
    int* color1 = (int*)malloc(n * sizeof(int)); int* color2 = (int*)malloc(m * sizeof(int));
    int c1[2], c2[2];
    bipartite(g1, n, color1, c1); bipartite(g2, m, color2, c2);
    int best2 = c2[0] > c2[1] ? c2[0] : c2[1];
    int* ans = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) ans[i] = c1[color1[i]] + best2;
    for (int i = 0; i < n; i++) free(g1[i].a); for (int i = 0; i < m; i++) free(g2[i].a);
    free(g1); free(g2); free(color1); free(color2);
    *returnSize = n; return ans;
}
