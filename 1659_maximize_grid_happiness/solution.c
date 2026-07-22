// LeetCode 1659 - Maximize Grid Happiness
// https://leetcode.com/problems/maximize-grid-happiness/

#include <stdlib.h>
#include <string.h>

static int pairCost(int a, int b) {
    if (!a || !b) return 0;
    return (a == 1 ? -30 : 20) + (b == 1 ? -30 : 20);
}

static int g_m, g_states, g_iMax, g_eMax;
static int *g_row, *g_compat, *g_intro, *g_extro, *g_memo;
static char *g_seen;

static int idx(int r, int prev, int i, int e) {
    return (((r * g_states + prev) * (g_iMax + 1) + i) * (g_eMax + 1) + e);
}

static int dfs(int r, int prev, int i, int e) {
    if (r == g_m) return 0;
    int id = idx(r, prev, i, e);
    if (g_seen[id]) return g_memo[id];
    int best = 0;
    for (int s = 0; s < g_states; s++) {
        if (g_intro[s] > i || g_extro[s] > e) continue;
        int val = g_row[s] + g_compat[prev * g_states + s] + dfs(r + 1, s, i - g_intro[s], e - g_extro[s]);
        if (val > best) best = val;
    }
    g_seen[id] = 1;
    g_memo[id] = best;
    return best;
}

int getMaxGridHappiness(int m, int n, int introvertsCount, int extrovertsCount) {
    int states = 1;
    for (int t = 0; t < n; t++) states *= 3;
    int (*cells)[5] = calloc((size_t)states, sizeof(*cells));
    int* intro = (int*)calloc((size_t)states, sizeof(int));
    int* extro = (int*)calloc((size_t)states, sizeof(int));
    int* row = (int*)calloc((size_t)states, sizeof(int));
    int* compat = (int*)calloc((size_t)states * (size_t)states, sizeof(int));

    for (int s = 0; s < states; s++) {
        int x = s;
        for (int j = 0; j < n; j++) {
            cells[s][j] = x % 3;
            x /= 3;
        }
        int val = 0;
        for (int j = 0; j < n; j++) {
            int z = cells[s][j];
            if (z == 1) { intro[s]++; val += 120; }
            else if (z == 2) { extro[s]++; val += 40; }
        }
        for (int j = 1; j < n; j++) val += pairCost(cells[s][j - 1], cells[s][j]);
        row[s] = val;
    }
    for (int a = 0; a < states; a++) {
        for (int b = 0; b < states; b++) {
            int v = 0;
            for (int j = 0; j < n; j++) v += pairCost(cells[a][j], cells[b][j]);
            compat[a * states + b] = v;
        }
    }

    int dims = (m + 1) * states * (introvertsCount + 1) * (extrovertsCount + 1);
    int* memo = (int*)malloc((size_t)dims * sizeof(int));
    char* seen = (char*)calloc((size_t)dims, 1);

    g_m = m; g_states = states; g_iMax = introvertsCount; g_eMax = extrovertsCount;
    g_row = row; g_compat = compat; g_intro = intro; g_extro = extro;
    g_memo = memo; g_seen = seen;

    int ans = dfs(0, 0, introvertsCount, extrovertsCount);

    free(cells); free(intro); free(extro); free(row); free(compat); free(memo); free(seen);
    return ans;
}
