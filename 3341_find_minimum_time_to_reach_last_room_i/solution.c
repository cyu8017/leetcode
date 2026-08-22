// LeetCode 3341 - Find Minimum Time to Reach Last Room I
// https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/

#include <stdlib.h>
#include <limits.h>

typedef struct { int t, r, c; } Node;

static void swapN(Node* a, Node* b) { Node t=*a;*a=*b;*b=t; }
static void up(Node* h, int i) {
    while (i > 0) { int p=(i-1)/2; if (h[i].t >= h[p].t) break; swapN(&h[i], &h[p]); i=p; }
}
static void down(Node* h, int n, int i) {
    for (;;) {
        int l=2*i+1,r=l+1,b=i;
        if (l<n && h[l].t < h[b].t) b=l;
        if (r<n && h[r].t < h[b].t) b=r;
        if (b==i) break; swapN(&h[i], &h[b]); i=b;
    }
}

int minTimeToReach(int** moveTime, int moveTimeSize, int* moveTimeColSize) {
    int m = moveTimeSize, n = moveTimeColSize[0];
    int** dist = (int**)malloc((size_t)m * sizeof(int*));
    for (int i = 0; i < m; i++) {
        dist[i] = (int*)malloc((size_t)n * sizeof(int));
        for (int j = 0; j < n; j++) dist[i][j] = INT_MAX / 4;
    }
    Node* h = (Node*)malloc((size_t)(m * n * 4 + 8) * sizeof(Node));
    int hn = 0;
    h[hn++] = (Node){0, 0, 0}; dist[0][0] = 0;
    int dirs[4][2] = {{0,1},{1,0},{0,-1},{-1,0}};
    while (hn > 0) {
        Node cur = h[0];
        h[0] = h[--hn]; if (hn) down(h, hn, 0);
        if (cur.t != dist[cur.r][cur.c]) continue;
        if (cur.r == m - 1 && cur.c == n - 1) {
            for (int i = 0; i < m; i++) free(dist[i]);
            free(dist); free(h);
            return cur.t;
        }
        for (int d = 0; d < 4; d++) {
            int nr = cur.r + dirs[d][0], nc = cur.c + dirs[d][1];
            if (nr < 0 || nc < 0 || nr >= m || nc >= n) continue;
            int start = cur.t;
            if (moveTime[nr][nc] > start) start = moveTime[nr][nc];
            int nt = start + 1;
            if (nt < dist[nr][nc]) {
                dist[nr][nc] = nt;
                h[hn] = (Node){nt, nr, nc}; up(h, hn++);
            }
        }
    }
    for (int i = 0; i < m; i++) free(dist[i]);
    free(dist); free(h);
    return -1;
}
