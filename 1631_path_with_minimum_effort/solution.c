// LeetCode 1631 - Path With Minimum Effort
// https://leetcode.com/problems/path-with-minimum-effort/

#include <stdlib.h>
#include <limits.h>

typedef struct { int effort; int i; int j; } Item;
typedef struct { Item* data; int size; int cap; } Heap;

static void ensure(Heap* h) {
    if (h->size < h->cap) return;
    h->cap = h->cap ? h->cap * 2 : 64;
    h->data = (Item*)realloc(h->data, (size_t)h->cap * sizeof(Item));
}
static void push(Heap* h, int effort, int i, int j) {
    ensure(h);
    int k = h->size++;
    h->data[k].effort = effort; h->data[k].i = i; h->data[k].j = j;
    while (k > 0) {
        int p = (k - 1) / 2;
        if (h->data[p].effort <= h->data[k].effort) break;
        Item t = h->data[p]; h->data[p] = h->data[k]; h->data[k] = t;
        k = p;
    }
}
static Item pop(Heap* h) {
    Item top = h->data[0];
    h->data[0] = h->data[--h->size];
    int k = 0;
    while (1) {
        int l = 2 * k + 1, r = l + 1, best = k;
        if (l < h->size && h->data[l].effort < h->data[best].effort) best = l;
        if (r < h->size && h->data[r].effort < h->data[best].effort) best = r;
        if (best == k) break;
        Item t = h->data[k]; h->data[k] = h->data[best]; h->data[best] = t;
        k = best;
    }
    return top;
}

int minimumEffortPath(int** heights, int heightsSize, int* heightsColSize) {
    int m = heightsSize, n = heightsColSize[0];
    int** dist = (int**)malloc((size_t)m * sizeof(int*));
    for (int i = 0; i < m; i++) {
        dist[i] = (int*)malloc((size_t)n * sizeof(int));
        for (int j = 0; j < n; j++) dist[i][j] = INT_MAX;
    }
    dist[0][0] = 0;
    Heap heap = {0};
    push(&heap, 0, 0, 0);
    int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
    int ans = 0;
    while (heap.size) {
        Item cur = pop(&heap);
        if (cur.i == m - 1 && cur.j == n - 1) { ans = cur.effort; break; }
        if (cur.effort != dist[cur.i][cur.j]) continue;
        for (int d = 0; d < 4; d++) {
            int x = cur.i + dirs[d][0], y = cur.j + dirs[d][1];
            if (x < 0 || x >= m || y < 0 || y >= n) continue;
            int diff = heights[cur.i][cur.j] - heights[x][y];
            if (diff < 0) diff = -diff;
            int nd = cur.effort > diff ? cur.effort : diff;
            if (nd < dist[x][y]) {
                dist[x][y] = nd;
                push(&heap, nd, x, y);
            }
        }
    }
    for (int i = 0; i < m; i++) free(dist[i]);
    free(dist); free(heap.data);
    return ans;
}
