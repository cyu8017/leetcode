// LeetCode 3562 - Maximum Profit from Trading Stocks with Discounts
// https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/

#include <stdlib.h>
#include <string.h>

static int imax(int a, int b) { return a > b ? a : b; }

static int* g_present;
static int* g_future;
static int** g;
static int* gSize;
static int g_budget;

static int* dfs(int u) {
    int* nxt = (int*)calloc((size_t)(g_budget + 1) * 2, sizeof(int));
    for (int ci = 0; ci < gSize[u]; ci++) {
        int v = g[u][ci];
        int* fv = dfs(v);
        for (int j = g_budget; j >= 0; j--) {
            for (int jv = 0; jv <= j; jv++) {
                for (int pre = 0; pre < 2; pre++) {
                    int idx = j * 2 + pre;
                    int cand = nxt[(j - jv) * 2 + pre] + fv[jv * 2 + pre];
                    if (cand > nxt[idx]) nxt[idx] = cand;
                }
            }
        }
        free(fv);
    }
    int* f = (int*)calloc((size_t)(g_budget + 1) * 2, sizeof(int));
    int price = g_future[u - 1];
    for (int j = 0; j <= g_budget; j++) {
        for (int pre = 0; pre < 2; pre++) {
            int cost = g_present[u - 1] / (pre + 1);
            if (j >= cost) {
                int buyProfit = nxt[(j - cost) * 2 + 1] + (price - cost);
                f[j * 2 + pre] = imax(nxt[j * 2 + 0], buyProfit);
            } else {
                f[j * 2 + pre] = nxt[j * 2 + 0];
            }
        }
    }
    free(nxt);
    return f;
}

int maxProfit(int n, int* present, int presentSize, int* future, int futureSize, int** hierarchy, int hierarchySize, int* hierarchyColSize, int budget) {
    (void)presentSize; (void)futureSize; (void)hierarchyColSize;
    g_present = present; g_future = future; g_budget = budget;
    g = (int**)calloc((size_t)(n + 1), sizeof(int*));
    gSize = (int*)calloc((size_t)(n + 1), sizeof(int));
    int* gCap = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int i = 0; i < hierarchySize; i++) {
        int u = hierarchy[i][0], v = hierarchy[i][1];
        if (gSize[u] == gCap[u]) {
            gCap[u] = gCap[u] ? gCap[u] * 2 : 4;
            g[u] = (int*)realloc(g[u], (size_t)gCap[u] * sizeof(int));
        }
        g[u][gSize[u]++] = v;
    }
    int* f = dfs(1);
    int ans = f[budget * 2 + 0];
    free(f);
    for (int i = 0; i <= n; i++) free(g[i]);
    free(g); free(gSize); free(gCap);
    return ans;
}
