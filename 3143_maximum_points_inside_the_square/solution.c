// LeetCode 3143 - Maximum Points Inside the Square
// https://leetcode.com/problems/maximum-points-inside-the-square/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

static int abs3143(int x) { return x < 0 ? -x : x; }
static int max4(int a, int b, int c, int d) {
    int m = a; if (b > m) m = b; if (c > m) m = c; if (d > m) m = d; return m;
}
static int cmp3143(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int maxPointsInsideSquare(int** points, int pointsSize, int* pointsColSize, char* s) {
    (void)pointsColSize;
    int* keys = malloc(pointsSize * sizeof(int));
    int** g = malloc(pointsSize * sizeof(int*));
    int* glen = calloc(pointsSize, sizeof(int));
    int* gcap = calloc(pointsSize, sizeof(int));
    int* keyOf = malloc(pointsSize * sizeof(int));
    int nk = 0;
    for (int i = 0; i < pointsSize; i++) {
        int key = max4(points[i][0], -points[i][0], points[i][1], -points[i][1]);
        int ki = -1;
        for (int t = 0; t < nk; t++) if (keys[t] == key) { ki = t; break; }
        if (ki < 0) { ki = nk; keys[nk++] = key; }
        if (glen[ki] == gcap[ki]) {
            gcap[ki] = gcap[ki] ? gcap[ki] * 2 : 4;
            g[ki] = realloc(g[ki], gcap[ki] * sizeof(int));
        }
        g[ki][glen[ki]++] = i;
        keyOf[i] = ki;
    }
    int* order = malloc(nk * sizeof(int));
    for (int i = 0; i < nk; i++) order[i] = i;
    /* sort by keys */
    for (int i = 0; i < nk; i++)
        for (int j = i + 1; j < nk; j++)
            if (keys[order[j]] < keys[order[i]]) {
                int t = order[i]; order[i] = order[j]; order[j] = t;
            }
    bool vis[26] = {0};
    int ans = 0;
    for (int oi = 0; oi < nk; oi++) {
        int ki = order[oi];
        bool fail = false;
        for (int t = 0; t < glen[ki]; t++) {
            int j = s[g[ki][t]] - 'a';
            if (vis[j]) { fail = true; break; }
            vis[j] = true;
        }
        if (fail) break;
        ans += glen[ki];
    }
    for (int i = 0; i < nk; i++) free(g[i]);
    free(g); free(glen); free(gcap); free(keys); free(keyOf); free(order);
    return ans;
}
