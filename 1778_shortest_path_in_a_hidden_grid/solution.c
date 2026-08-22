// LeetCode 1778 - Shortest Path in a Hidden Grid
// https://leetcode.com/problems/shortest-path-in-a-hidden-grid/

#include <stdlib.h>

int findShortestPath(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize;
    int n = gridColSize[0];
    int sr = 0, sc = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == -1) {
                sr = i;
                sc = j;
            }
        }
    }

    static const int DIRS[4][2] = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
    int* dist = (int*)malloc((size_t)(m * n) * sizeof(int));
    for (int i = 0; i < m * n; i++) {
        dist[i] = -1;
    }
    int* queue = (int*)malloc((size_t)(m * n) * sizeof(int));
    int head = 0, tail = 0;
    dist[sr * n + sc] = 0;
    queue[tail++] = sr * n + sc;
    while (head < tail) {
        int cur = queue[head++];
        int r = cur / n;
        int c = cur % n;
        if (grid[r][c] == 2) {
            int result = dist[cur];
            free(dist);
            free(queue);
            return result;
        }
        for (int d = 0; d < 4; d++) {
            int nr = r + DIRS[d][0];
            int nc = c + DIRS[d][1];
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] != 0 &&
                dist[nr * n + nc] < 0) {
                dist[nr * n + nc] = dist[cur] + 1;
                queue[tail++] = nr * n + nc;
            }
        }
    }
    free(dist);
    free(queue);
    return -1;
}
