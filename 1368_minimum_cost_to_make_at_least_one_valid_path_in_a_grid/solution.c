// LeetCode 1368 - Minimum Cost to Make at Least One Valid Path in a Grid
// https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/

#include <stdlib.h>

int minCost(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    int INF = 1000000000;
    int* dist = (int*)malloc(m * n * sizeof(int));
    for (int i = 0; i < m * n; i++) dist[i] = INF;
    dist[0] = 0;
    int* dq = (int*)malloc(m * n * 2 * sizeof(int));
    int head = m * n, tail = m * n;
    dq[tail++] = 0;
    int dirs[4][2] = {{0,1},{0,-1},{1,0},{-1,0}};
    while (head < tail) {
        int cur = dq[head++];
        int r = cur / n, c = cur % n;
        for (int k = 0; k < 4; k++) {
            int x = r + dirs[k][0], y = c + dirs[k][1];
            if (x < 0 || x >= m || y < 0 || y >= n) continue;
            int w = (k + 1) != grid[r][c];
            int nd = dist[cur] + w;
            int ni = x * n + y;
            if (nd < dist[ni]) {
                dist[ni] = nd;
                if (w) dq[tail++] = ni;
                else dq[--head] = ni;
            }
        }
    }
    int ans = dist[m * n - 1];
    free(dist); free(dq);
    return ans;
}
