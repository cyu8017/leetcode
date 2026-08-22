// LeetCode 2322 - Minimum Score After Removals on a Tree
// https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/

#include <stdlib.h>
#include <string.h>

static int* G_head;
static int* G_to;
static int* G_next;
static int* G_xor;
static int* G_in;
static int* G_out;
static int* G_nums;
static int G_time;

static void dfs_score(int u, int p) {
    G_in[u] = G_time++;
    G_xor[u] = G_nums[u];
    for (int e = G_head[u]; e != -1; e = G_next[e]) {
        int v = G_to[e];
        if (v == p) continue;
        dfs_score(v, u);
        G_xor[u] ^= G_xor[v];
    }
    G_out[u] = G_time;
}

static int is_anc(int a, int b) {
    return G_in[a] <= G_in[b] && G_out[b] <= G_out[a];
}

int minimumScore(int* nums, int numsSize, int** edges, int edgesSize, int* edgesColSize) {
    (void)edgesColSize;
    int n = numsSize;
    G_nums = nums;
    G_head = (int*)malloc((size_t)n * sizeof(int));
    memset(G_head, -1, (size_t)n * sizeof(int));
    G_to = (int*)malloc((size_t)edgesSize * 2 * sizeof(int));
    G_next = (int*)malloc((size_t)edgesSize * 2 * sizeof(int));
    int ec = 0;
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1];
        G_to[ec] = v; G_next[ec] = G_head[u]; G_head[u] = ec++;
        G_to[ec] = u; G_next[ec] = G_head[v]; G_head[v] = ec++;
    }
    G_xor = (int*)malloc((size_t)n * sizeof(int));
    G_in = (int*)malloc((size_t)n * sizeof(int));
    G_out = (int*)malloc((size_t)n * sizeof(int));
    G_time = 0;
    dfs_score(0, -1);
    int total = G_xor[0];
    int ans = 1 << 30;
    for (int i = 1; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int a, b, c;
            if (is_anc(i, j)) {
                a = G_xor[j]; b = G_xor[i] ^ G_xor[j]; c = total ^ G_xor[i];
            } else if (is_anc(j, i)) {
                a = G_xor[i]; b = G_xor[j] ^ G_xor[i]; c = total ^ G_xor[j];
            } else {
                a = G_xor[i]; b = G_xor[j]; c = total ^ G_xor[i] ^ G_xor[j];
            }
            int mx = a > b ? a : b; if (c > mx) mx = c;
            int mn = a < b ? a : b; if (c < mn) mn = c;
            if (mx - mn < ans) ans = mx - mn;
        }
    }
    free(G_head); free(G_to); free(G_next); free(G_xor); free(G_in); free(G_out);
    return ans;
}
