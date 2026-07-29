// LeetCode 0778 - Swim in Rising Water
#include <stdlib.h>
#include <stdbool.h>

typedef struct { int t, r, c; } Node;

static void swapN(Node* a, Node* b) { Node t=*a; *a=*b; *b=t; }

static void push(Node* h, int* sz, Node v) {
    int i = (*sz)++;
    h[i] = v;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h[p].t <= h[i].t) break;
        swapN(&h[p], &h[i]); i = p;
    }
}

static Node pop(Node* h, int* sz) {
    Node top = h[0];
    h[0] = h[--(*sz)];
    int i = 0;
    while (1) {
        int l = i*2+1, r = l+1, s = i;
        if (l < *sz && h[l].t < h[s].t) s = l;
        if (r < *sz && h[r].t < h[s].t) s = r;
        if (s == i) break;
        swapN(&h[i], &h[s]); i = s;
    }
    return top;
}

int swimInWater(int** grid, int gridSize, int* gridColSize) {
    (void)gridColSize;
    int n = gridSize;
    bool* seen = (bool*)calloc((size_t)n * n, sizeof(bool));
    Node* heap = (Node*)malloc((size_t)n * n * sizeof(Node));
    int hsz = 0;
    push(heap, &hsz, (Node){grid[0][0], 0, 0});
    seen[0] = true;
    int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
    while (hsz) {
        Node cur = pop(heap, &hsz);
        if (cur.r == n - 1 && cur.c == n - 1) { free(seen); free(heap); return cur.t; }
        for (int d = 0; d < 4; d++) {
            int nr = cur.r + dirs[d][0], nc = cur.c + dirs[d][1];
            if (nr < 0 || nr >= n || nc < 0 || nc >= n || seen[nr * n + nc]) continue;
            seen[nr * n + nc] = true;
            int nt = cur.t > grid[nr][nc] ? cur.t : grid[nr][nc];
            push(heap, &hsz, (Node){nt, nr, nc});
        }
    }
    free(seen); free(heap); return -1;
}
