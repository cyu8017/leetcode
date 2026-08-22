// LeetCode 3123 - Find Edges in Shortest Paths
// https://leetcode.com/problems/find-edges-in-shortest-paths/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct { int b, w, i; } E3123;
typedef struct { int dis, u; } P3123;

bool* findAnswer(int n, int** edges, int edgesSize, int* edgesColSize, int* returnSize) {
    (void)edgesColSize;
    E3123** g = calloc(n, sizeof(E3123*));
    int* glen = calloc(n, sizeof(int));
    int* gcap = calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int a = edges[i][0], b = edges[i][1], w = edges[i][2];
        for (int t = 0; t < 2; t++) {
            int u = t ? b : a, v = t ? a : b;
            if (glen[u] == gcap[u]) {
                gcap[u] = gcap[u] ? gcap[u] * 2 : 4;
                g[u] = realloc(g[u], gcap[u] * sizeof(E3123));
            }
            g[u][glen[u]++] = (E3123){v, w, i};
        }
    }
    const int INF = 1 << 30;
    int* dist = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) dist[i] = INF;
    dist[0] = 0;
    P3123* pq = malloc((edgesSize * 4 + n + 8) * sizeof(P3123));
    int psz = 0;
    pq[psz++] = (P3123){0, 0};
    while (psz) {
        int bi = 0;
        for (int i = 1; i < psz; i++) if (pq[i].dis < pq[bi].dis) bi = i;
        P3123 p = pq[bi]; pq[bi] = pq[--psz];
        if (p.dis > dist[p.u]) continue;
        for (int i = 0; i < glen[p.u]; i++) {
            int b = g[p.u][i].b, w = g[p.u][i].w;
            if (dist[b] > dist[p.u] + w) {
                dist[b] = dist[p.u] + w;
                pq[psz++] = (P3123){dist[b], b};
            }
        }
    }
    bool* ans = calloc(edgesSize, sizeof(bool));
    *returnSize = edgesSize;
    if (dist[n - 1] != INF) {
        int* q = malloc(n * 2 * sizeof(int));
        int qh = 0, qt = 0;
        bool* seen = calloc(n, sizeof(bool));
        q[qt++] = n - 1; seen[n - 1] = true;
        while (qh < qt) {
            int a = q[qh++];
            for (int i = 0; i < glen[a]; i++) {
                int b = g[a][i].b, w = g[a][i].w, ei = g[a][i].i;
                if (dist[a] == dist[b] + w) {
                    ans[ei] = true;
                    if (!seen[b]) { seen[b] = true; q[qt++] = b; }
                }
            }
        }
        free(q); free(seen);
    }
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(glen); free(gcap); free(dist); free(pq);
    return ans;
}
