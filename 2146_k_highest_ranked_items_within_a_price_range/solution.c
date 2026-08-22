// LeetCode 2146 - K Highest Ranked Items Within a Price Range
// https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

typedef struct { int dist, price, r, c; } Item;

static int cmpItem(const void* a, const void* b) {
    const Item *x = a, *y = b;
    if (x->dist != y->dist) return x->dist - y->dist;
    if (x->price != y->price) return x->price - y->price;
    if (x->r != y->r) return x->r - y->r;
    return x->c - y->c;
}

int** highestRankedKItems(int** grid, int gridSize, int* gridColSize, int* pricing, int pricingSize, int* start, int startSize, int k, int* returnSize, int** returnColumnSizes) {
    (void)pricingSize; (void)startSize;
    int m = gridSize, n = gridColSize[0];
    int low = pricing[0], high = pricing[1];
    bool** vis = (bool**)malloc((size_t)m * sizeof(bool*));
    for (int i = 0; i < m; i++) vis[i] = (bool*)calloc((size_t)n, sizeof(bool));
    int *qr = (int*)malloc((size_t)m * n * sizeof(int));
    int *qc = (int*)malloc((size_t)m * n * sizeof(int));
    int *qd = (int*)malloc((size_t)m * n * sizeof(int));
    int qh = 0, qt = 0;
    qr[qt] = start[0]; qc[qt] = start[1]; qd[qt] = 0; qt++;
    vis[start[0]][start[1]] = true;
    Item* cands = (Item*)malloc((size_t)m * n * sizeof(Item));
    int cn = 0;
    int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
    while (qh < qt) {
        int r = qr[qh], c = qc[qh], d = qd[qh]; qh++;
        if (grid[r][c] >= low && grid[r][c] <= high)
            cands[cn++] = (Item){d, grid[r][c], r, c};
        for (int t = 0; t < 4; t++) {
            int nr = r + dirs[t][0], nc = c + dirs[t][1];
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && !vis[nr][nc] && grid[nr][nc] != 0) {
                vis[nr][nc] = true;
                qr[qt] = nr; qc[qt] = nc; qd[qt] = d + 1; qt++;
            }
        }
    }
    qsort(cands, (size_t)cn, sizeof(Item), cmpItem);
    if (k > cn) k = cn;
    int** ans = (int**)malloc((size_t)k * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)k * sizeof(int));
    for (int i = 0; i < k; i++) {
        ans[i] = (int*)malloc(2 * sizeof(int));
        ans[i][0] = cands[i].r; ans[i][1] = cands[i].c;
        (*returnColumnSizes)[i] = 2;
    }
    for (int i = 0; i < m; i++) free(vis[i]);
    free(vis); free(qr); free(qc); free(qd); free(cands);
    *returnSize = k;
    return ans;
}
