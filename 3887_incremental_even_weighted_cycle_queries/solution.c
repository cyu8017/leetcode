// LeetCode 3887 - Incremental Even-Weighted Cycle Queries
// https://leetcode.com/problems/incremental-even-weighted-cycle-queries/

#include <stdlib.h>

static int find3887(int* parent, int* parity, int x, int* pout) {
    int res = 0;
    while (parent[x] != x) {
        res ^= parity[x];
        x = parent[x];
    }
    *pout = res;
    return x;
}

int countValidEdges(int n, int** edges, int edgesSize, int* edgesColSize) {
    (void)edgesColSize;
    int* parent = malloc((size_t)n * sizeof(int));
    int* size = malloc((size_t)n * sizeof(int));
    int* parity = calloc((size_t)n, sizeof(int));
    for (int i = 0; i < n; i++) { parent[i] = i; size[i] = 1; }
    int ans = 0;
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1], w = edges[i][2];
        int pu, pv;
        int ru = find3887(parent, parity, u, &pu);
        int rv = find3887(parent, parity, v, &pv);
        if (ru == rv) {
            if ((pu ^ pv) == w) ans++;
            continue;
        }
        if (size[ru] < size[rv]) {
            int t = ru; ru = rv; rv = t;
            t = pu; pu = pv; pv = t;
        }
        parent[rv] = ru;
        parity[rv] = pu ^ pv ^ w;
        size[ru] += size[rv];
        ans++;
    }
    free(parent); free(size); free(parity);
    return ans;
}
