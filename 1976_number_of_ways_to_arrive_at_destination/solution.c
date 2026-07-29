// LeetCode 1976 - Number of Ways to Arrive at Destination
// https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

#include <stdlib.h>
#include <limits.h>

typedef struct { long long d; int u; } Node;

static void push(Node** h, int* sz, int* cap, Node v) {
    if (*sz >= *cap) { *cap = *cap ? *cap * 2 : 16; *h = (Node*)realloc(*h, (size_t)(*cap) * sizeof(Node)); }
    int i = (*sz)++;
    (*h)[i] = v;
    while (i > 0) {
        int p = (i - 1) / 2;
        if ((*h)[p].d <= (*h)[i].d) break;
        Node t = (*h)[p]; (*h)[p] = (*h)[i]; (*h)[i] = t;
        i = p;
    }
}

static Node pop(Node* h, int* sz) {
    Node top = h[0];
    h[0] = h[--(*sz)];
    int i = 0;
    while (1) {
        int l = 2 * i + 1, r = 2 * i + 2, best = i;
        if (l < *sz && h[l].d < h[best].d) best = l;
        if (r < *sz && h[r].d < h[best].d) best = r;
        if (best == i) break;
        Node t = h[i]; h[i] = h[best]; h[best] = t;
        i = best;
    }
    return top;
}

int countPaths(int n, int** roads, int roadsSize, int* roadsColSize) {
    (void)roadsColSize;
    const int MOD = 1000000007;
    int** to = (int**)calloc((size_t)n, sizeof(int*));
    int** wt = (int**)calloc((size_t)n, sizeof(int*));
    int* deg = (int*)calloc((size_t)n, sizeof(int));
    int* cap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < roadsSize; i++) {
        int u = roads[i][0], v = roads[i][1], t = roads[i][2];
        for (int rep = 0; rep < 2; rep++) {
            if (deg[u] == cap[u]) {
                cap[u] = cap[u] ? cap[u] * 2 : 4;
                to[u] = (int*)realloc(to[u], (size_t)cap[u] * sizeof(int));
                wt[u] = (int*)realloc(wt[u], (size_t)cap[u] * sizeof(int));
            }
            to[u][deg[u]] = v; wt[u][deg[u]] = t; deg[u]++;
            int tmp = u; u = v; v = tmp;
        }
    }
    long long* dist = (long long*)malloc((size_t)n * sizeof(long long));
    int* ways = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < n; i++) dist[i] = LLONG_MAX / 4;
    dist[0] = 0; ways[0] = 1;
    Node* heap = NULL; int hsz = 0, hcap = 0;
    push(&heap, &hsz, &hcap, (Node){0, 0});
    while (hsz) {
        Node cur = pop(heap, &hsz);
        if (cur.d > dist[cur.u]) continue;
        for (int i = 0; i < deg[cur.u]; i++) {
            int v = to[cur.u][i];
            long long nd = cur.d + wt[cur.u][i];
            if (nd < dist[v]) {
                dist[v] = nd;
                ways[v] = ways[cur.u];
                push(&heap, &hsz, &hcap, (Node){nd, v});
            } else if (nd == dist[v]) {
                ways[v] = (ways[v] + ways[cur.u]) % MOD;
            }
        }
    }
    int ans = ways[n - 1];
    for (int i = 0; i < n; i++) { free(to[i]); free(wt[i]); }
    free(to); free(wt); free(deg); free(cap); free(dist); free(ways); free(heap);
    return ans;
}
