// LeetCode 3342 - Find Minimum Time to Reach Last Room II
// https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/

#include <stdlib.h>
#include <string.h>

typedef struct { int t, r, c, parity; } Node3342;

static void swap_n(Node3342* a, Node3342* b) { Node3342 t = *a; *a = *b; *b = t; }

static void heap_up(Node3342* h, int i) {
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h[p].t <= h[i].t) break;
        swap_n(&h[p], &h[i]);
        i = p;
    }
}

static void heap_down(Node3342* h, int n, int i) {
    for (;;) {
        int l = 2 * i + 1, r = 2 * i + 2, s = i;
        if (l < n && h[l].t < h[s].t) s = l;
        if (r < n && h[r].t < h[s].t) s = r;
        if (s == i) break;
        swap_n(&h[s], &h[i]);
        i = s;
    }
}

int minTimeToReach(int** moveTime, int moveTimeSize, int* moveTimeColSize) {
    (void)moveTimeColSize;
    int m = moveTimeSize, n = moveTime[0] ? 0 : 0;
    n = moveTimeColSize ? moveTimeColSize[0] : 0;
    if (!moveTimeColSize) {
        /* fallback: assume rectangular from first row length unknown; use moveTimeSize cols via param */
    }
    /* LeetCode passes col sizes */
    n = moveTimeColSize[0];
    int INF = 1 << 30;
    int*** dist = (int***)malloc(m * sizeof(int**));
    for (int i = 0; i < m; i++) {
        dist[i] = (int**)malloc(n * sizeof(int*));
        for (int j = 0; j < n; j++) {
            dist[i][j] = (int*)malloc(2 * sizeof(int));
            dist[i][j][0] = dist[i][j][1] = INF;
        }
    }
    int cap = m * n * 4 + 16, hn = 0;
    Node3342* heap = (Node3342*)malloc(cap * sizeof(Node3342));
    heap[hn++] = (Node3342){0, 0, 0, 0};
    dist[0][0][0] = 0;
    int dirs[4][2] = {{0,1},{1,0},{0,-1},{-1,0}};
    int ans = -1;
    while (hn > 0) {
        Node3342 cur = heap[0];
        heap[0] = heap[--hn];
        if (hn) heap_down(heap, hn, 0);
        if (cur.t != dist[cur.r][cur.c][cur.parity]) continue;
        if (cur.r == m - 1 && cur.c == n - 1) { ans = cur.t; break; }
        int cost = cur.parity == 1 ? 2 : 1;
        for (int d = 0; d < 4; d++) {
            int nr = cur.r + dirs[d][0], nc = cur.c + dirs[d][1];
            if (nr < 0 || nc < 0 || nr >= m || nc >= n) continue;
            int start = cur.t;
            if (moveTime[nr][nc] > start) start = moveTime[nr][nc];
            int nt = start + cost;
            int np = 1 - cur.parity;
            if (nt < dist[nr][nc][np]) {
                dist[nr][nc][np] = nt;
                if (hn + 1 >= cap) {
                    cap *= 2;
                    heap = (Node3342*)realloc(heap, cap * sizeof(Node3342));
                }
                heap[hn] = (Node3342){nt, nr, nc, np};
                heap_up(heap, hn);
                hn++;
            }
        }
    }
    free(heap);
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) free(dist[i][j]);
        free(dist[i]);
    }
    free(dist);
    return ans;
}
