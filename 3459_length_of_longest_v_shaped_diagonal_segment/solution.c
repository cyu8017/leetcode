// LeetCode 3459 - Length of Longest V-Shaped Diagonal Segment
// https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/

#include <stdlib.h>
#include <string.h>

static int dirs[4][2] = {{1, 1}, {1, -1}, {-1, -1}, {-1, 1}};
static int nextDir[4] = {1, 2, 3, 0};
static int ***memo5; /* too heavy - use flat hash via recursive with memo array */
static int *memo;
static int M, N, MEMO_STRIDE;
static int **G;

static int key5(int i, int j, int d, int turned, int expect) {
    /* expect is 0 or 2 -> map 0->0, 2->1 */
    int e = (expect == 2) ? 1 : 0;
    return ((((i * N + j) * 4 + d) * 2 + turned) * 2 + e);
}

static int dfs(int i, int j, int d, int turned, int expect) {
    if (i < 0 || j < 0 || i >= M || j >= N || G[i][j] != expect) return 0;
    int k = key5(i, j, d, turned, expect);
    if (memo[k] != -1) return memo[k];
    int ni = i + dirs[d][0], nj = j + dirs[d][1];
    int nx = (expect == 2) ? 0 : 2;
    int best = 1 + dfs(ni, nj, d, turned, nx);
    if (turned == 0) {
        int nd = nextDir[d];
        int ti = i + dirs[nd][0], tj = j + dirs[nd][1];
        int cand = 1 + dfs(ti, tj, nd, 1, nx);
        if (cand > best) best = cand;
    }
    memo[k] = best;
    return best;
}

int lenOfVDiagonal(int** grid, int gridSize, int* gridColSize) {
    M = gridSize; N = gridColSize[0]; G = grid;
    int memoSize = M * N * 4 * 2 * 2;
    memo = (int*)malloc((size_t)memoSize * sizeof(int));
    for (int i = 0; i < memoSize; i++) memo[i] = -1;
    int ans = 0;
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            if (grid[i][j] != 1) continue;
            for (int d = 0; d < 4; d++) {
                int ni = i + dirs[d][0], nj = j + dirs[d][1];
                int best = 1 + dfs(ni, nj, d, 0, 2);
                if (best > ans) ans = best;
            }
            if (ans < 1) ans = 1;
        }
    }
    free(memo);
    return ans;
}
