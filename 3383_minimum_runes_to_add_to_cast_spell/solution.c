// LeetCode 3383 - Minimum Runes to Add to Cast Spell
// https://leetcode.com/problems/minimum-runes-to-add-to-cast-spell/

#include <stdlib.h>
#include <stdbool.h>

typedef struct { int* a; int n, cap; } Adj;
static void adj_push(Adj* g, int u, int v) {
    if (g[u].n == g[u].cap) { g[u].cap = g[u].cap ? g[u].cap * 2 : 4; g[u].a = (int*)realloc(g[u].a, g[u].cap * sizeof(int)); }
    g[u].a[g[u].n++] = v;
}
static Adj* Gg; static bool* vis; static int* order; static int on;
static void dfs1(int u) {
    vis[u] = true;
    for (int i = 0; i < Gg[u].n; i++) if (!vis[Gg[u].a[i]]) dfs1(Gg[u].a[i]);
    order[on++] = u;
}
static Adj* Rg; static int* comp; static int cid;
static void dfs2(int u) {
    comp[u] = cid;
    for (int i = 0; i < Rg[u].n; i++) if (comp[Rg[u].a[i]] == -1) dfs2(Rg[u].a[i]);
}

int minRunesToAdd(int n, int* crystals, int crystalsSize, int* flowFrom, int flowFromSize, int* flowTo, int flowToSize) {
    (void)flowToSize;
    Gg = (Adj*)calloc(n, sizeof(Adj)); Rg = (Adj*)calloc(n, sizeof(Adj));
    for (int i = 0; i < flowFromSize; i++) { adj_push(Gg, flowFrom[i], flowTo[i]); adj_push(Rg, flowTo[i], flowFrom[i]); }
    vis = (bool*)calloc(n, 1); order = (int*)malloc(n * sizeof(int)); on = 0;
    for (int i = 0; i < n; i++) if (!vis[i]) dfs1(i);
    comp = (int*)malloc(n * sizeof(int)); for (int i = 0; i < n; i++) comp[i] = -1; cid = 0;
    for (int i = n - 1; i >= 0; i--) if (comp[order[i]] == -1) { dfs2(order[i]); cid++; }
    bool* hasCrystal = (bool*)calloc(cid, 1);
    for (int i = 0; i < crystalsSize; i++) hasCrystal[comp[crystals[i]]] = true;
    int* indeg = (int*)calloc(cid, sizeof(int));
    for (int u = 0; u < n; u++) for (int i = 0; i < Gg[u].n; i++) {
        int v = Gg[u].a[i]; if (comp[u] != comp[v]) indeg[comp[v]]++;
    }
    int ans = 0;
    for (int i = 0; i < cid; i++) if (indeg[i] == 0 && !hasCrystal[i]) ans++;
    for (int i = 0; i < n; i++) { free(Gg[i].a); free(Rg[i].a); }
    free(Gg); free(Rg); free(vis); free(order); free(comp); free(hasCrystal); free(indeg);
    return ans;
}
