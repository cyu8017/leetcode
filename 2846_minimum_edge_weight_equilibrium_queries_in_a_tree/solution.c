// LeetCode 2846 - Minimum Edge Weight Equilibrium Queries in a Tree
// https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/

#include <stdlib.h>
#include <string.h>

int* minOperationsQueries(int n, int** edges, int edgesSize, int* edgesColSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)edgesColSize; (void)queriesColSize;
    int* deg = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) { deg[edges[i][0]]++; deg[edges[i][1]]++; }
    int** gu = (int**)malloc(n * sizeof(int*));
    int** gw = (int**)malloc(n * sizeof(int*));
    int* gsz = (int*)calloc(n, sizeof(int));
    int* fill = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < n; i++) {
        gu[i] = (int*)malloc(deg[i] * sizeof(int));
        gw[i] = (int*)malloc(deg[i] * sizeof(int));
    }
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1], w = edges[i][2];
        gu[u][fill[u]] = v; gw[u][fill[u]] = w; fill[u]++;
        gu[v][fill[v]] = u; gw[v][fill[v]] = w; fill[v]++;
    }
    for (int i = 0; i < n; i++) gsz[i] = fill[i];
    const int LOG = 15;
    int** up = (int**)malloc(LOG * sizeof(int*));
    for (int j = 0; j < LOG; j++) up[j] = (int*)calloc(n, sizeof(int));
    int* depth = (int*)calloc(n, sizeof(int));
    int(*cnt)[27] = calloc(n, sizeof(int[27]));
    int* stack = (int*)malloc(n * sizeof(int));
    int* pstack = (int*)malloc(n * sizeof(int));
    int top = 0;
    stack[top] = 0; pstack[top] = 0; top++;
    // iterative DFS
    int* order = (int*)malloc(n * sizeof(int));
    int* parent = (int*)malloc(n * sizeof(int));
    int oc = 0;
    int* st = (int*)malloc(n * sizeof(int));
    int* it = (int*)calloc(n, sizeof(int));
    int stp = 0;
    st[stp++] = 0;
    parent[0] = 0;
    up[0][0] = 0;
    while (stp) {
        int u = st[stp - 1];
        if (it[u] == 0) order[oc++] = u;
        if (it[u] < gsz[u]) {
            int v = gu[u][it[u]], w = gw[u][it[u]];
            it[u]++;
            if (v == parent[u]) continue;
            parent[v] = u;
            up[0][v] = u;
            depth[v] = depth[u] + 1;
            memcpy(cnt[v], cnt[u], sizeof(int[27]));
            cnt[v][w]++;
            st[stp++] = v;
        } else stp--;
    }
    for (int j = 1; j < LOG; j++)
        for (int i = 0; i < n; i++)
            up[j][i] = up[j - 1][up[j - 1][i]];

    int* ans = (int*)malloc(queriesSize * sizeof(int));
    for (int qi = 0; qi < queriesSize; qi++) {
        int a = queries[qi][0], b = queries[qi][1];
        int aa = a, bb = b;
        if (depth[aa] < depth[bb]) { int t = aa; aa = bb; bb = t; }
        int diff = depth[aa] - depth[bb];
        for (int j = 0; j < LOG; j++) if (diff & (1 << j)) aa = up[j][aa];
        int c;
        if (aa == bb) c = aa;
        else {
            for (int j = LOG - 1; j >= 0; j--) {
                if (up[j][aa] != up[j][bb]) {
                    aa = up[j][aa]; bb = up[j][bb];
                }
            }
            c = up[0][aa];
        }
        int total = depth[a] + depth[b] - 2 * depth[c];
        int best = 0;
        for (int w = 1; w <= 26; w++) {
            int f = cnt[a][w] + cnt[b][w] - 2 * cnt[c][w];
            if (f > best) best = f;
        }
        ans[qi] = total - best;
    }
    for (int i = 0; i < n; i++) { free(gu[i]); free(gw[i]); }
    free(gu); free(gw); free(deg); free(gsz); free(fill);
    for (int j = 0; j < LOG; j++) free(up[j]);
    free(up); free(depth); free(cnt); free(stack); free(pstack);
    free(order); free(parent); free(st); free(it);
    *returnSize = queriesSize;
    return ans;
}
