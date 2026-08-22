// LeetCode 2467 - Most Profitable Path in a Tree
// https://leetcode.com/problems/most-profitable-path-in-a-tree/

#include <stdlib.h>
#include <string.h>
#include <limits.h>

static int** g2467;
static int* deg2467;
static int* cap2467;
static int* bobTime2467;
static int* amount2467;
static int ans2467;

static void add_edge(int a, int b) {
    if (deg2467[a] == cap2467[a]) {
        cap2467[a] = cap2467[a] ? cap2467[a] * 2 : 4;
        g2467[a] = (int*)realloc(g2467[a], (size_t)cap2467[a] * sizeof(int));
    }
    g2467[a][deg2467[a]++] = b;
}

static int findBob(int u, int p, int t) {
    if (u == 0) { bobTime2467[u] = t; return 1; }
    for (int i = 0; i < deg2467[u]; i++) {
        int v = g2467[u][i];
        if (v == p) continue;
        if (findBob(v, u, t + 1)) { bobTime2467[u] = t; return 1; }
    }
    return 0;
}

static void dfsAlice(int u, int p, int t, int income) {
    int cur = amount2467[u];
    if (t > bobTime2467[u]) cur = 0;
    else if (t == bobTime2467[u]) cur /= 2;
    income += cur;
    int isLeaf = 1;
    for (int i = 0; i < deg2467[u]; i++) {
        int v = g2467[u][i];
        if (v != p) {
            isLeaf = 0;
            dfsAlice(v, u, t + 1, income);
        }
    }
    if (isLeaf && income > ans2467) ans2467 = income;
}

int mostProfitablePath(int** edges, int edgesSize, int* edgesColSize, int bob, int* amount, int amountSize) {
    (void)edgesColSize;
    int n = amountSize;
    g2467 = (int**)calloc((size_t)n, sizeof(int*));
    deg2467 = (int*)calloc((size_t)n, sizeof(int));
    cap2467 = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        add_edge(edges[i][0], edges[i][1]);
        add_edge(edges[i][1], edges[i][0]);
    }
    bobTime2467 = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) bobTime2467[i] = n;
    amount2467 = amount;
    findBob(bob, -1, 0);
    ans2467 = INT_MIN / 2;
    dfsAlice(0, -1, 0, 0);
    int result = ans2467;
    for (int i = 0; i < n; i++) free(g2467[i]);
    free(g2467); free(deg2467); free(cap2467); free(bobTime2467);
    return result;
}
