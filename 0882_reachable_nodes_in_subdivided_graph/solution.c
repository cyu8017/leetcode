// LeetCode 0882 - Reachable Nodes In Subdivided Graph
// https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/

#include <stdlib.h>
#include <stdbool.h>

#define MIN(a,b) ((a)<(b)?(a):(b))

typedef struct { int v, cnt; } Edge;
typedef struct { int moves, node; } Item;

int reachableNodes(int** edges, int edgesSize, int* edgesColSize, int maxMoves, int n) {
    (void)edgesColSize;
    Edge** g = (Edge**)calloc((size_t)n, sizeof(Edge*));
    int* gsz = (int*)calloc((size_t)n, sizeof(int));
    int* gcap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1], cnt = edges[i][2];
        for (int t = 0; t < 2; t++) {
            int a = t ? v : u, b = t ? u : v;
            if (gsz[a] == gcap[a]) {
                gcap[a] = gcap[a] ? gcap[a] * 2 : 2;
                g[a] = (Edge*)realloc(g[a], (size_t)gcap[a] * sizeof(Edge));
            }
            g[a][gsz[a]++] = (Edge){b, cnt};
        }
    }
    int* seen = (int*)malloc((size_t)n * sizeof(int));
    bool* vis = (bool*)calloc((size_t)n, sizeof(bool));
    for (int i = 0; i < n; i++) seen[i] = -1;
    Item* heap = (Item*)malloc((size_t)(n * 8 + 16) * sizeof(Item));
    int hs = 0;

    heap[hs++] = (Item){maxMoves, 0};
    while (hs) {
        // pop max moves
        int bi = 0;
        for (int i = 1; i < hs; i++) if (heap[i].moves > heap[bi].moves) bi = i;
        Item cur = heap[bi];
        heap[bi] = heap[--hs];
        if (vis[cur.node]) continue;
        vis[cur.node] = true;
        seen[cur.node] = cur.moves;
        for (int i = 0; i < gsz[cur.node]; i++) {
            int nei = g[cur.node][i].v, cnt = g[cur.node][i].cnt;
            int remain = cur.moves - cnt - 1;
            if (!vis[nei] && remain >= 0) heap[hs++] = (Item){remain, nei};
        }
    }
    int ans = 0;
    for (int i = 0; i < n; i++) if (seen[i] >= 0) ans++;
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1], cnt = edges[i][2];
        int a = seen[u] >= 0 ? seen[u] : 0;
        int b = seen[v] >= 0 ? seen[v] : 0;
        ans += MIN(cnt, a + b);
    }
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(gsz); free(gcap); free(seen); free(vis); free(heap);
    return ans;
}
