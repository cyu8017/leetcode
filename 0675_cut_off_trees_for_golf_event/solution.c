// LeetCode 0675 - Cut Off Trees for Golf Event
// https://leetcode.com/problems/cut-off-trees-for-golf-event/

#include <stdlib.h>
#include <string.h>

typedef struct { int h, r, c; } Tree;
static int cmpTree(const void* a, const void* b) { return ((const Tree*)a)->h - ((const Tree*)b)->h; }

static int bfs(int** forest, int m, int n, int sr, int sc, int tr, int tc) {
    if (sr == tr && sc == tc) return 0;
    int* seen = (int*)calloc((size_t)m * n, sizeof(int));
    int* qr = (int*)malloc((size_t)m * n * sizeof(int));
    int* qc = (int*)malloc((size_t)m * n * sizeof(int));
    int* qd = (int*)malloc((size_t)m * n * sizeof(int));
    int head = 0, tail = 0;
    qr[tail]=sr; qc[tail]=sc; qd[tail]=0; tail++;
    seen[sr * n + sc] = 1;
    int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
    while (head < tail) {
        int r = qr[head], c = qc[head], d = qd[head]; head++;
        for (int i = 0; i < 4; i++) {
            int nr = r + dirs[i][0], nc = c + dirs[i][1];
            if (nr < 0 || nc < 0 || nr >= m || nc >= n) continue;
            if (seen[nr * n + nc] || forest[nr][nc] == 0) continue;
            if (nr == tr && nc == tc) {
                free(seen); free(qr); free(qc); free(qd);
                return d + 1;
            }
            seen[nr * n + nc] = 1;
            qr[tail]=nr; qc[tail]=nc; qd[tail]=d+1; tail++;
        }
    }
    free(seen); free(qr); free(qc); free(qd);
    return -1;
}

int cutOffTree(int** forest, int forestSize, int* forestColSize) {
    int m = forestSize, n = forestColSize[0];
    Tree trees[2500];
    int tcount = 0;
    for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) if (forest[i][j] > 1) {
        trees[tcount].h = forest[i][j]; trees[tcount].r = i; trees[tcount].c = j; tcount++;
    }
    qsort(trees, (size_t)tcount, sizeof(Tree), cmpTree);
    int sr = 0, sc = 0, steps = 0;
    for (int i = 0; i < tcount; i++) {
        int dist = bfs(forest, m, n, sr, sc, trees[i].r, trees[i].c);
        if (dist < 0) return -1;
        steps += dist;
        sr = trees[i].r; sc = trees[i].c;
    }
    return steps;
}
