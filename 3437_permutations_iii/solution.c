// LeetCode 3437 - Permutations III
// https://leetcode.com/problems/permutations-iii/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static int** g_ans; static int g_an, g_acap, g_n;
static int* g_cur; static bool* g_used;

static void dfs3437(void) {
    if (g_cur[0] /* misuse */) {}
    int len = 0; while (len < g_n && g_cur[len] != 0) len++;
    /* track length separately */
}

/* rewrite with length param via static depth */
static int g_depth;

static void dfs_perm(void) {
    if (g_depth == g_n) {
        if (g_an == g_acap) {
            g_acap = g_acap ? g_acap * 2 : 8;
            g_ans = (int**)realloc(g_ans, g_acap * sizeof(int*));
        }
        g_ans[g_an] = (int*)malloc(g_n * sizeof(int));
        memcpy(g_ans[g_an], g_cur, g_n * sizeof(int));
        g_an++;
        return;
    }
    for (int i = 1; i <= g_n; i++) {
        if (g_used[i]) continue;
        if (g_depth > 0 && (g_cur[g_depth - 1] % 2 == i % 2)) continue;
        g_used[i] = true;
        g_cur[g_depth++] = i;
        dfs_perm();
        g_depth--;
        g_used[i] = false;
    }
}

int** permute(int n, int* returnSize, int** returnColumnSizes) {
    g_n = n; g_an = 0; g_acap = 0; g_ans = NULL; g_depth = 0;
    g_cur = (int*)calloc(n, sizeof(int));
    g_used = (bool*)calloc(n + 1, sizeof(bool));
    dfs_perm();
    *returnSize = g_an;
    *returnColumnSizes = (int*)malloc(g_an * sizeof(int));
    for (int i = 0; i < g_an; i++) (*returnColumnSizes)[i] = n;
    free(g_cur); free(g_used);
    return g_ans;
}
