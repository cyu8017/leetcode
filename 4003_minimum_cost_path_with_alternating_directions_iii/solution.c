// LeetCode 4003 - Minimum Cost Path With Alternating Directions III
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-iii/

#include <stdlib.h>
#include <stdint.h>
#include <limits.h>

#define INF4003 ((int64_t)1 << 60)

typedef struct {
    int64_t d;
    int i, j, k;
} Tup4003;

typedef struct {
    Tup4003* a;
    int n, cap;
} Heap4003;

static void heapSwap(Tup4003* x, Tup4003* y) {
    Tup4003 t = *x;
    *x = *y;
    *y = t;
}

static void heapPush(Heap4003* h, Tup4003 v) {
    if (h->n == h->cap) {
        h->cap = h->cap ? h->cap * 2 : 64;
        h->a = (Tup4003*)realloc(h->a, (size_t)h->cap * sizeof(Tup4003));
    }
    int i = h->n++;
    h->a[i] = v;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h->a[p].d <= h->a[i].d) break;
        heapSwap(&h->a[p], &h->a[i]);
        i = p;
    }
}

static Tup4003 heapPop(Heap4003* h) {
    Tup4003 v = h->a[0];
    h->a[0] = h->a[--h->n];
    int i = 0;
    for (;;) {
        int l = 2 * i + 1, r = l + 1, s = i;
        if (l < h->n && h->a[l].d < h->a[s].d) s = l;
        if (r < h->n && h->a[r].d < h->a[s].d) s = r;
        if (s == i) break;
        heapSwap(&h->a[s], &h->a[i]);
        i = s;
    }
    return v;
}

long long minCost(int m, int n, int** penalty, int penaltySize, int* penaltyColSize) {
    (void)penaltySize;
    (void)penaltyColSize;
    int64_t*** dist = (int64_t***)malloc((size_t)m * sizeof(int64_t**));
    for (int i = 0; i < m; i++) {
        dist[i] = (int64_t**)malloc((size_t)n * sizeof(int64_t*));
        for (int j = 0; j < n; j++) {
            dist[i][j] = (int64_t*)malloc(2 * sizeof(int64_t));
            dist[i][j][0] = INF4003;
            dist[i][j][1] = INF4003;
        }
    }
    dist[0][0][1] = 1;
    Heap4003 pq = {NULL, 0, 0};
    heapPush(&pq, (Tup4003){1, 0, 0, 1});
    int dirs[4][2] = {{-1, 0}, {0, 1}, {0, -1}, {1, 0}};
    int64_t ans = -1;

    while (pq.n > 0) {
        Tup4003 cur = heapPop(&pq);
        int64_t d = cur.d;
        int i = cur.i, j = cur.j, k = cur.k;
        if (i == m - 1 && j == n - 1) {
            ans = d;
            break;
        }
        if (d > dist[i][j][k]) continue;
        int p = penalty[i][j];
        int64_t nd = d + (int64_t)p;
        if (nd < dist[i][j][k ^ 1]) {
            dist[i][j][k ^ 1] = nd;
            heapPush(&pq, (Tup4003){nd, i, j, k ^ 1});
        }
        for (int idx = 0; idx < 4; idx++) {
            int x = i + dirs[idx][0], y = j + dirs[idx][1];
            if (0 <= x && x < m && 0 <= y && y < n) {
                nd = d + (int64_t)((x + 1) * (y + 1) + (((idx & 1) ^ k) * p));
                if (nd < dist[x][y][k ^ 1]) {
                    dist[x][y][k ^ 1] = nd;
                    heapPush(&pq, (Tup4003){nd, x, y, k ^ 1});
                }
            }
        }
    }

    free(pq.a);
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) free(dist[i][j]);
        free(dist[i]);
    }
    free(dist);
    return ans;
}
