// LeetCode 2493 - Divide Nodes Into the Maximum Number of Groups
// https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/

#include <stdlib.h>
#include <string.h>

static int** g2493;
static int* deg2493;
static int* cap2493;
static int n2493;

static void add2493(int a, int b) {
    if (deg2493[a] == cap2493[a]) {
        cap2493[a] = cap2493[a] ? cap2493[a] * 2 : 4;
        g2493[a] = (int*)realloc(g2493[a], (size_t)cap2493[a] * sizeof(int));
    }
    g2493[a][deg2493[a]++] = b;
}

static int bfsDepth2493(int start) {
    int* dist = (int*)malloc((size_t)(n2493 + 1) * sizeof(int));
    for (int i = 0; i <= n2493; i++) dist[i] = -1;
    int* q = (int*)malloc((size_t)(n2493 + 5) * sizeof(int));
    int head = 0, tail = 0;
    q[tail++] = start;
    dist[start] = 1;
    int best = 1;
    while (head < tail) {
        int u = q[head++];
        if (dist[u] > best) best = dist[u];
        for (int i = 0; i < deg2493[u]; i++) {
            int v = g2493[u][i];
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q[tail++] = v;
            }
        }
    }
    free(dist); free(q);
    return best;
}

int magnificentSets(int n, int** edges, int edgesSize, int* edgesColSize) {
    (void)edgesColSize;
    n2493 = n;
    g2493 = (int**)calloc((size_t)(n + 1), sizeof(int*));
    deg2493 = (int*)calloc((size_t)(n + 1), sizeof(int));
    cap2493 = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        add2493(edges[i][0], edges[i][1]);
        add2493(edges[i][1], edges[i][0]);
    }
    int* color = (int*)malloc((size_t)(n + 1) * sizeof(int));
    for (int i = 0; i <= n; i++) color[i] = -1;
    int** comps = (int**)malloc((size_t)n * sizeof(int*));
    int* compSz = (int*)malloc((size_t)n * sizeof(int));
    int cc = 0;
    int* q = (int*)malloc((size_t)(n + 5) * sizeof(int));
    for (int i = 1; i <= n; i++) {
        if (color[i] != -1) continue;
        int* comp = (int*)malloc((size_t)n * sizeof(int));
        int csz = 0, head = 0, tail = 0;
        q[tail++] = i;
        color[i] = 0;
        int bipartite = 1;
        while (head < tail) {
            int u = q[head++];
            comp[csz++] = u;
            for (int j = 0; j < deg2493[u]; j++) {
                int v = g2493[u][j];
                if (color[v] == -1) {
                    color[v] = color[u] ^ 1;
                    q[tail++] = v;
                } else if (color[v] == color[u]) bipartite = 0;
            }
        }
        if (!bipartite) {
            free(comp); free(color); free(q);
            for (int t = 0; t < cc; t++) free(comps[t]);
            free(comps); free(compSz);
            for (int t = 0; t <= n; t++) free(g2493[t]);
            free(g2493); free(deg2493); free(cap2493);
            return -1;
        }
        comps[cc] = comp;
        compSz[cc] = csz;
        cc++;
    }
    free(color); free(q);
    int ans = 0;
    for (int c = 0; c < cc; c++) {
        int best = 0;
        for (int i = 0; i < compSz[c]; i++) {
            int d = bfsDepth2493(comps[c][i]);
            if (d > best) best = d;
        }
        ans += best;
        free(comps[c]);
    }
    free(comps); free(compSz);
    for (int i = 0; i <= n; i++) free(g2493[i]);
    free(g2493); free(deg2493); free(cap2493);
    return ans;
}
