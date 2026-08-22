// LeetCode 2440 - Create Components With Same Value
// https://leetcode.com/problems/create-components-with-same-value/

#include <stdlib.h>
#include <string.h>

static int* g_nums;
static int** g_adj;
static int* g_deg;
static int* g_cap;

static int dfs2440(int u, int p, int target) {
    int sum = g_nums[u];
    for (int i = 0; i < g_deg[u]; i++) {
        int v = g_adj[u][i];
        if (v == p) continue;
        int sub = dfs2440(v, u, target);
        if (sub < 0) return -1;
        sum += sub;
    }
    if (sum > target) return -1;
    if (sum == target) return 0;
    return sum;
}

int componentValue(int* nums, int numsSize, int** edges, int edgesSize, int* edgesColSize) {
    (void)edgesColSize;
    int n = numsSize;
    int total = 0;
    for (int i = 0; i < n; i++) total += nums[i];
    g_nums = nums;
    g_adj = (int**)calloc((size_t)n, sizeof(int*));
    g_deg = (int*)calloc((size_t)n, sizeof(int));
    g_cap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int a = edges[i][0], b = edges[i][1];
        if (g_deg[a] == g_cap[a]) {
            g_cap[a] = g_cap[a] ? g_cap[a] * 2 : 4;
            g_adj[a] = (int*)realloc(g_adj[a], (size_t)g_cap[a] * sizeof(int));
        }
        g_adj[a][g_deg[a]++] = b;
        if (g_deg[b] == g_cap[b]) {
            g_cap[b] = g_cap[b] ? g_cap[b] * 2 : 4;
            g_adj[b] = (int*)realloc(g_adj[b], (size_t)g_cap[b] * sizeof(int));
        }
        g_adj[b][g_deg[b]++] = a;
    }
    int ans = 0;
    for (int parts = n; parts >= 1; parts--) {
        if (total % parts != 0) continue;
        int target = total / parts;
        if (dfs2440(0, -1, target) == 0) {
            ans = parts - 1;
            break;
        }
    }
    for (int i = 0; i < n; i++) free(g_adj[i]);
    free(g_adj);
    free(g_deg);
    free(g_cap);
    return ans;
}
