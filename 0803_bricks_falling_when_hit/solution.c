// LeetCode 0803 - Bricks Falling When Hit
// https://leetcode.com/problems/bricks-falling-when-hit/

#include <stdlib.h>
#include <string.h>

#define MAX(a,b) ((a)>(b)?(a):(b))

static int findp(int* parent, int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

static void unite(int* parent, int* size, int a, int b) {
    int ra = findp(parent, a), rb = findp(parent, b);
    if (ra == rb) return;
    parent[ra] = rb;
    size[rb] += size[ra];
}

int* hitBricks(int** grid, int gridSize, int* gridColSize, int** hits, int hitsSize, int* hitsColSize, int* returnSize) {
    (void)hitsColSize;
    int m = gridSize, n = gridColSize[0];
    int roof = m * n;
    int N = roof + 1;
    int* parent = (int*)malloc((size_t)N * sizeof(int));
    int* size = (int*)malloc((size_t)N * sizeof(int));
    for (int i = 0; i < N; i++) { parent[i] = i; size[i] = 1; }

    int* status = (int*)malloc((size_t)m * (size_t)n * sizeof(int));
    for (int r = 0; r < m; r++)
        for (int c = 0; c < n; c++)
            status[r * n + c] = grid[r][c];
    for (int i = 0; i < hitsSize; i++)
        status[hits[i][0] * n + hits[i][1]] = 0;

    int dr[4] = {-1,1,0,0}, dc[4] = {0,0,-1,1};
    for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++) {
            if (!status[r * n + c]) continue;
            int id = r * n + c;
            if (r == 0) unite(parent, size, id, roof);
            for (int k = 0; k < 4; k++) {
                int nr = r + dr[k], nc = c + dc[k];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && status[nr * n + nc])
                    unite(parent, size, id, nr * n + nc);
            }
        }
    }

    int* answer = (int*)calloc((size_t)hitsSize, sizeof(int));
    for (int i = hitsSize - 1; i >= 0; i--) {
        int r = hits[i][0], c = hits[i][1];
        if (grid[r][c] == 0) continue;
        int prev = size[findp(parent, roof)];
        status[r * n + c] = 1;
        int id = r * n + c;
        if (r == 0) unite(parent, size, id, roof);
        for (int k = 0; k < 4; k++) {
            int nr = r + dr[k], nc = c + dc[k];
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && status[nr * n + nc])
                unite(parent, size, id, nr * n + nc);
        }
        int curr = size[findp(parent, roof)];
        answer[i] = MAX(0, curr - prev - 1);
    }
    free(parent); free(size); free(status);
    *returnSize = hitsSize;
    return answer;
}
