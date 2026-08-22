// LeetCode 2581 - Count Number of Possible Root Nodes
// https://leetcode.com/problems/count-number-of-possible-root-nodes/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

typedef struct { int u, v; } EdgePair;

static int* adj_head;
static int* adj_to;
static int* adj_next;
static int edge_cnt;
static int n_nodes;
static int ans2581;
static int k2581;

static void add_edge(int u, int v) {
    adj_to[edge_cnt] = v;
    adj_next[edge_cnt] = adj_head[u];
    adj_head[u] = edge_cnt++;
}

static long long pack(int u, int v) { return ((long long)u << 32) | (unsigned)v; }

typedef struct { long long key; bool set; } GH;
static GH* ghash;
static int gcap;

static void gput(int u, int v) {
    long long key = pack(u, v);
    unsigned h = (unsigned)(key ^ (key >> 33)) & (gcap - 1);
    while (ghash[h].set && ghash[h].key != key) h = (h + 1) & (gcap - 1);
    ghash[h].set = true; ghash[h].key = key;
}
static bool ghas(int u, int v) {
    long long key = pack(u, v);
    unsigned h = (unsigned)(key ^ (key >> 33)) & (gcap - 1);
    while (ghash[h].set) {
        if (ghash[h].key == key) return true;
        h = (h + 1) & (gcap - 1);
    }
    return false;
}

static int dfs1(int u, int p) {
    int cnt = 0;
    for (int e = adj_head[u]; e != -1; e = adj_next[e]) {
        int v = adj_to[e];
        if (v == p) continue;
        if (ghas(u, v)) cnt++;
        cnt += dfs1(v, u);
    }
    return cnt;
}

static void dfs2(int u, int p, int cur) {
    if (cur >= k2581) ans2581++;
    for (int e = adj_head[u]; e != -1; e = adj_next[e]) {
        int v = adj_to[e];
        if (v == p) continue;
        int nxt = cur;
        if (ghas(u, v)) nxt--;
        if (ghas(v, u)) nxt++;
        dfs2(v, u, nxt);
    }
}

int rootCount(int** edges, int edgesSize, int* edgesColSize, int** guesses, int guessesSize, int* guessesColSize, int k) {
    (void)edgesColSize; (void)guessesColSize;
    n_nodes = edgesSize + 1;
    k2581 = k;
    ans2581 = 0;
    adj_head = (int*)malloc((size_t)n_nodes * sizeof(int));
    for (int i = 0; i < n_nodes; i++) adj_head[i] = -1;
    adj_to = (int*)malloc((size_t)(2 * edgesSize) * sizeof(int));
    adj_next = (int*)malloc((size_t)(2 * edgesSize) * sizeof(int));
    edge_cnt = 0;
    for (int i = 0; i < edgesSize; i++) {
        add_edge(edges[i][0], edges[i][1]);
        add_edge(edges[i][1], edges[i][0]);
    }
    gcap = 1;
    while (gcap < guessesSize * 4 + 16) gcap <<= 1;
    ghash = (GH*)calloc((size_t)gcap, sizeof(GH));
    for (int i = 0; i < guessesSize; i++) gput(guesses[i][0], guesses[i][1]);
    int base = dfs1(0, -1);
    dfs2(0, -1, base);
    free(adj_head); free(adj_to); free(adj_next); free(ghash);
    return ans2581;
}
