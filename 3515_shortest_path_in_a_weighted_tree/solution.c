// LeetCode 3515 - Shortest Path in a Weighted Tree
// https://leetcode.com/problems/shortest-path-in-a-weighted-tree/

#include <stdlib.h>

static int* bit3515;
static int n3515;

static void add3515(int i, int v) {
    for (; i <= n3515; i += i & -i) bit3515[i] += v;
}
static void rangeAdd3515(int l, int r, int v) {
    add3515(l + 1, v);
    add3515(r + 2, -v);
}
static int point3515(int i) {
    int s = 0;
    i++;
    for (; i > 0; i -= i & -i) s += bit3515[i];
    return s;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* treeQueries(int n, int** edges, int edgesSize, int* edgesColSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)edgesColSize; (void)queriesColSize;
    n3515 = n;
    int** gto = (int**)calloc((size_t)(n + 1), sizeof(int*));
    int** gw = (int**)calloc((size_t)(n + 1), sizeof(int*));
    int* gsz = (int*)calloc((size_t)(n + 1), sizeof(int));
    int* gcap = (int*)calloc((size_t)(n + 1), sizeof(int));
    int* wu = (int*)malloc((size_t)edgesSize * sizeof(int));
    int* wv = (int*)malloc((size_t)edgesSize * sizeof(int));
    int* ww = (int*)malloc((size_t)edgesSize * sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1], w = edges[i][2];
        wu[i] = u < v ? u : v; wv[i] = u < v ? v : u; ww[i] = w;
        for (int rep = 0; rep < 2; rep++) {
            int a = rep ? v : u, b = rep ? u : v;
            if (gsz[a] == gcap[a]) {
                gcap[a] = gcap[a] ? gcap[a] * 2 : 2;
                gto[a] = (int*)realloc(gto[a], (size_t)gcap[a] * sizeof(int));
                gw[a] = (int*)realloc(gw[a], (size_t)gcap[a] * sizeof(int));
            }
            gto[a][gsz[a]] = b; gw[a][gsz[a]] = w; gsz[a]++;
        }
    }
    int* inT = (int*)calloc((size_t)(n + 1), sizeof(int));
    int* outT = (int*)calloc((size_t)(n + 1), sizeof(int));
    int* dist = (int*)calloc((size_t)(n + 1), sizeof(int));
    int* parent = (int*)calloc((size_t)(n + 1), sizeof(int));
    int* stacku = (int*)malloc((size_t)(n + 2) * sizeof(int));
    int* stackp = (int*)malloc((size_t)(n + 2) * sizeof(int));
    int* stacki = (int*)malloc((size_t)(n + 2) * sizeof(int));
    int stp = 0, time = 0;
    stacku[stp] = 1; stackp[stp] = 0; stacki[stp] = -2; stp++;
    while (stp) {
        stp--;
        int u = stacku[stp], p = stackp[stp], ii = stacki[stp];
        if (ii == -2) {
            inT[u] = time++;
            stacku[stp] = u; stackp[stp] = p; stacki[stp] = -1; stp++;
            for (int e = gsz[u] - 1; e >= 0; e--) {
                int v = gto[u][e];
                if (v == p) continue;
                parent[v] = u;
                dist[v] = dist[u] + gw[u][e];
                stacku[stp] = v; stackp[stp] = u; stacki[stp] = -2; stp++;
            }
        } else outT[u] = time - 1;
    }
    bit3515 = (int*)calloc((size_t)(n + 3), sizeof(int));
    for (int i = 1; i <= n; i++) rangeAdd3515(inT[i], inT[i], dist[i]);
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    int ac = 0;
    for (int qi = 0; qi < queriesSize; qi++) {
        if (queries[qi][0] == 1) {
            int u = queries[qi][1], v = queries[qi][2], nw = queries[qi][3];
            int a = u < v ? u : v, b = u < v ? v : u;
            int ow = 0;
            for (int i = 0; i < edgesSize; i++) if (wu[i] == a && wv[i] == b) { ow = ww[i]; ww[i] = nw; break; }
            int child = (parent[u] == v) ? u : v;
            rangeAdd3515(inT[child], outT[child], nw - ow);
        } else ans[ac++] = point3515(inT[queries[qi][1]]);
    }
    for (int i = 0; i <= n; i++) { free(gto[i]); free(gw[i]); }
    free(gto); free(gw); free(gsz); free(gcap);
    free(wu); free(wv); free(ww); free(inT); free(outT); free(dist); free(parent);
    free(stacku); free(stackp); free(stacki); free(bit3515);
    *returnSize = ac;
    return ans;
}
