// LeetCode 2097 - Valid Arrangement of Pairs
// https://leetcode.com/problems/valid-arrangement-of-pairs/

#include <stdlib.h>
#include <string.h>

typedef struct { int* a; int n, cap; } Vec2097;
typedef struct { int key; Vec2097 v; int used; int indeg, outdeg; } Node2097;

static unsigned h2097(int k) { return (unsigned)k * 2654435761u; }

typedef struct {
    Node2097* tab;
    int cap;
} Graph2097;

static Node2097* gFind(Graph2097* g, int key, int create) {
    int idx = (int)(h2097(key) & (unsigned)(g->cap - 1));
    for (;;) {
        if (!g->tab[idx].used) {
            if (!create) return NULL;
            g->tab[idx].used = 1;
            g->tab[idx].key = key;
            g->tab[idx].v.a = NULL; g->tab[idx].v.n = 0; g->tab[idx].v.cap = 0;
            g->tab[idx].indeg = g->tab[idx].outdeg = 0;
            return &g->tab[idx];
        }
        if (g->tab[idx].key == key) return &g->tab[idx];
        idx = (idx + 1) & (g->cap - 1);
    }
}

static void vecPush(Vec2097* v, int x) {
    if (v->n == v->cap) {
        v->cap = v->cap ? v->cap * 2 : 4;
        v->a = (int*)realloc(v->a, (size_t)v->cap * sizeof(int));
    }
    v->a[v->n++] = x;
}

static int* path2097;
static int pathN2097;
static Graph2097* G2097;

static void dfs2097(int u) {
    Node2097* node = gFind(G2097, u, 0);
    while (node && node->v.n > 0) {
        int v = node->v.a[--node->v.n];
        dfs2097(v);
    }
    path2097[pathN2097++] = u;
}

int** validArrangement(int** pairs, int pairsSize, int* pairsColSize, int* returnSize, int** returnColumnSizes) {
    (void)pairsColSize;
    int cap = 1;
    while (cap < pairsSize * 4 + 16) cap *= 2;
    Graph2097 g = {0};
    g.cap = cap;
    g.tab = (Node2097*)calloc((size_t)cap, sizeof(Node2097));
    G2097 = &g;
    for (int i = 0; i < pairsSize; i++) {
        int u = pairs[i][0], v = pairs[i][1];
        Node2097* nu = gFind(&g, u, 1);
        Node2097* nv = gFind(&g, v, 1);
        vecPush(&nu->v, v);
        nu->outdeg++;
        nv->indeg++;
    }
    int start = pairs[0][0];
    for (int i = 0; i < cap; i++) if (g.tab[i].used) {
        if (g.tab[i].outdeg - g.tab[i].indeg == 1) { start = g.tab[i].key; break; }
    }
    path2097 = (int*)malloc((size_t)(pairsSize + 2) * sizeof(int));
    pathN2097 = 0;
    dfs2097(start);
    for (int i = 0, j = pathN2097 - 1; i < j; i++, j--) {
        int t = path2097[i]; path2097[i] = path2097[j]; path2097[j] = t;
    }
    int m = pathN2097 - 1;
    int** ans = (int**)malloc((size_t)m * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)m * sizeof(int));
    for (int i = 0; i < m; i++) {
        ans[i] = (int*)malloc(2 * sizeof(int));
        ans[i][0] = path2097[i];
        ans[i][1] = path2097[i + 1];
        (*returnColumnSizes)[i] = 2;
    }
    *returnSize = m;
    for (int i = 0; i < cap; i++) if (g.tab[i].used) free(g.tab[i].v.a);
    free(g.tab); free(path2097);
    return ans;
}
