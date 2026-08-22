// LeetCode 3459 - Length of Longest V-Shaped Diagonal Segment
// https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/

#include <stdlib.h>

static int dirs3459[4][2] = {{1, 1}, {1, -1}, {-1, -1}, {-1, 1}};
static int nextDir3459[4] = {1, 2, 3, 0};
static int* memo3459;
static int M3459, N3459;
static int** G3459;

static int key3459(int i, int j, int d, int turned, int expect) {
    int e = (expect == 2) ? 1 : 0;
    return ((((i * N3459 + j) * 4 + d) * 2 + turned) * 2 + e);
}

static int dfs3459(int i, int j, int d, int turned, int expect) {
    if (i < 0 || j < 0 || i >= M3459 || j >= N3459 || G3459[i][j] != expect) return 0;
    int k = key3459(i, j, d, turned, expect);
    if (memo3459[k] != -1) return memo3459[k];
    int ni = i + dirs3459[d][0], nj = j + dirs3459[d][1];
    int nx = (expect == 2) ? 0 : 2;
    int best = 1 + dfs3459(ni, nj, d, turned, nx);
    if (turned == 0) {
        int nd = nextDir3459[d];
        int ti = i + dirs3459[nd][0], tj = j + dirs3459[nd][1];
        int cand = 1 + dfs3459(ti, tj, nd, 1, nx);
        if (cand > best) best = cand;
    }
    memo3459[k] = best;
    return best;
}

int lenOfVDiagonal(int** grid, int gridSize, int* gridColSize) {
    M3459 = gridSize;
    N3459 = gridColSize[0];
    G3459 = grid;
    int memoSize = M3459 * N3459 * 4 * 2 * 2;
    memo3459 = (int*)malloc((size_t)memoSize * sizeof(int));
    for (int i = 0; i < memoSize; i++) memo3459[i] = -1;
    int ans = 0;
    for (int i = 0; i < M3459; i++) {
        for (int j = 0; j < N3459; j++) {
            if (grid[i][j] != 1) continue;
            for (int d = 0; d < 4; d++) {
                int ni = i + dirs3459[d][0], nj = j + dirs3459[d][1];
                int best = 1 + dfs3459(ni, nj, d, 0, 2);
                if (best > ans) ans = best;
            }
            if (ans < 1) ans = 1;
        }
    }
    free(memo3459);
    return ans;
}
