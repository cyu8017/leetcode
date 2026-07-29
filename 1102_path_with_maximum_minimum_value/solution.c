// LeetCode 1102 - Path With Maximum Minimum Value
// https://leetcode.com/problems/path-with-maximum-minimum-value/

#include <stdlib.h>

typedef struct { int val, r, c; } Node;

static void heapSwap(Node* a, Node* b) { Node t = *a; *a = *b; *b = t; }

static void heapPush(Node* heap, int* size, Node item) {
    int i = (*size)++;
    heap[i] = item;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (heap[p].val >= heap[i].val) break;
        heapSwap(&heap[p], &heap[i]);
        i = p;
    }
}

static Node heapPop(Node* heap, int* size) {
    Node top = heap[0];
    heap[0] = heap[--(*size)];
    int i = 0;
    while (1) {
        int l = 2 * i + 1, r = 2 * i + 2, best = i;
        if (l < *size && heap[l].val > heap[best].val) best = l;
        if (r < *size && heap[r].val > heap[best].val) best = r;
        if (best == i) break;
        heapSwap(&heap[best], &heap[i]);
        i = best;
    }
    return top;
}

int maximumMinimumPath(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    char* seen = (char*)calloc((size_t)m * (size_t)n, 1);
    Node* heap = (Node*)malloc((size_t)m * (size_t)n * sizeof(Node));
    int hsize = 0;
    heapPush(heap, &hsize, (Node){grid[0][0], 0, 0});
    seen[0] = 1;
    int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
    while (hsize) {
        Node cur = heapPop(heap, &hsize);
        if (cur.r == m - 1 && cur.c == n - 1) {
            free(seen); free(heap);
            return cur.val;
        }
        for (int d = 0; d < 4; d++) {
            int nr = cur.r + dirs[d][0], nc = cur.c + dirs[d][1];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
            if (seen[nr * n + nc]) continue;
            seen[nr * n + nc] = 1;
            int nv = cur.val < grid[nr][nc] ? cur.val : grid[nr][nc];
            heapPush(heap, &hsize, (Node){nv, nr, nc});
        }
    }
    free(seen); free(heap);
    return grid[0][0];
}
