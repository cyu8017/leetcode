// LeetCode 2876 - Count Visited Nodes in a Directed Graph
// https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/

#include <stdlib.h>
#include <string.h>

static int* g_edges;
static int* g_ans;
static int* g_state;
static int* g_stack;
static int g_top;

static void dfs(int u) {
    g_state[u] = 1;
    g_stack[g_top++] = u;
    int v = g_edges[u];
    if (g_state[v] == 0) dfs(v);
    else if (g_state[v] == 1) {
        int idx = g_top - 1;
        while (g_stack[idx] != v) idx--;
        int cyc = g_top - idx;
        for (int i = idx; i < g_top; i++) g_ans[g_stack[i]] = cyc;
    }
    if (g_ans[u] == 0) g_ans[u] = g_ans[g_edges[u]] + 1;
    g_state[u] = 2;
    g_top--;
}

int* countVisitedNodes(int* edges, int edgesSize, int* returnSize) {
    int n = edgesSize;
    g_edges = edges;
    g_ans = (int*)calloc(n, sizeof(int));
    g_state = (int*)calloc(n, sizeof(int));
    g_stack = (int*)malloc(n * sizeof(int));
    g_top = 0;
    for (int i = 0; i < n; i++) if (g_state[i] == 0) dfs(i);
    free(g_state); free(g_stack);
    *returnSize = n;
    return g_ans;
}
