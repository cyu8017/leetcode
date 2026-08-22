// LeetCode 1293 - Shortest Path in a Grid with Obstacles Elimination
// https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

#include <stdlib.h>

typedef struct {
    int r, c, rem, dist;
} Node;

int shortestPath(int** grid, int gridSize, int* gridColSize, int k) {
    int m = gridSize, n = gridColSize[0];
    if (k >= m + n - 2) return m + n - 2;
    int states = m * n * (k + 1);
    int* best = (int*)malloc((size_t)states * sizeof(int));
    for (int i = 0; i < states; i++) best[i] = -1;
    Node* queue = (Node*)malloc((size_t)(m * n * (k + 1)) * sizeof(Node));
    int head = 0, tail = 0;
    queue[tail++] = (Node){0, 0, k, 0};
    best[0 * (k + 1) + k] = k;
    static const int dr[4] = {1, -1, 0, 0};
    static const int dc[4] = {0, 0, 1, -1};
    while (head < tail) {
        Node cur = queue[head++];
        if (cur.r == m - 1 && cur.c == n - 1) {
            int ans = cur.dist;
            free(best);
            free(queue);
            return ans;
        }
        for (int d = 0; d < 4; d++) {
            int nr = cur.r + dr[d], nc = cur.c + dc[d];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
            int nrem = cur.rem - grid[nr][nc];
            if (nrem < 0) continue;
            int idx = (nr * n + nc) * (k + 1) + nrem;
            if (nrem <= best[idx]) continue;
            best[idx] = nrem;
            queue[tail++] = (Node){nr, nc, nrem, cur.dist + 1};
        }
    }
    free(best);
    free(queue);
    return -1;
}
