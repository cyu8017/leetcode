// LeetCode 1810 - Minimum Path Cost in a Hidden Grid
// https://leetcode.com/problems/minimum-path-cost-in-a-hidden-grid/

#include <limits.h>
#include <stdlib.h>

typedef struct {
    int dist;
    int r;
    int c;
} HeapNode;

typedef struct {
    HeapNode* data;
    int size;
    int capacity;
} MinHeap;

static void heapEnsure(MinHeap* h) {
    if (h->size < h->capacity) return;
    h->capacity = h->capacity ? h->capacity * 2 : 16;
    h->data = (HeapNode*)realloc(h->data, (size_t)h->capacity * sizeof(HeapNode));
}

static void heapPush(MinHeap* h, int dist, int r, int c) {
    heapEnsure(h);
    int i = h->size++;
    h->data[i].dist = dist;
    h->data[i].r = r;
    h->data[i].c = c;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h->data[p].dist <= h->data[i].dist) break;
        HeapNode t = h->data[p];
        h->data[p] = h->data[i];
        h->data[i] = t;
        i = p;
    }
}

static HeapNode heapPop(MinHeap* h) {
    HeapNode top = h->data[0];
    h->data[0] = h->data[--h->size];
    int i = 0;
    while (1) {
        int l = 2 * i + 1, r = l + 1, best = i;
        if (l < h->size && h->data[l].dist < h->data[best].dist) best = l;
        if (r < h->size && h->data[r].dist < h->data[best].dist) best = r;
        if (best == i) break;
        HeapNode t = h->data[i];
        h->data[i] = h->data[best];
        h->data[best] = t;
        i = best;
    }
    return top;
}

int findShortestPath(int** grid, int gridSize, int* gridColSize, int r1, int c1, int r2, int c2) {
    if (r1 == r2 && c1 == c2) return 0;
    int m = gridSize;
    int n = gridColSize[0];
    static const int DIRS[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    int** dist = (int**)malloc((size_t)m * sizeof(int*));
    for (int i = 0; i < m; i++) {
        dist[i] = (int*)malloc((size_t)n * sizeof(int));
        for (int j = 0; j < n; j++) dist[i][j] = INT_MAX;
    }

    MinHeap heap = {0};
    dist[r1][c1] = 0;
    heapPush(&heap, 0, r1, c1);

    int answer = -1;
    while (heap.size) {
        HeapNode cur = heapPop(&heap);
        if (cur.r == r2 && cur.c == c2) {
            answer = cur.dist;
            break;
        }
        if (cur.dist > dist[cur.r][cur.c]) continue;
        for (int d = 0; d < 4; d++) {
            int nr = cur.r + DIRS[d][0];
            int nc = cur.c + DIRS[d][1];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 0) continue;
            int nd = cur.dist + grid[nr][nc];
            if (nd < dist[nr][nc]) {
                dist[nr][nc] = nd;
                heapPush(&heap, nd, nr, nc);
            }
        }
    }

    free(heap.data);
    for (int i = 0; i < m; i++) free(dist[i]);
    free(dist);
    return answer;
}
