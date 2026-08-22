// LeetCode 3905 - Multi Source Flood Fill
// https://leetcode.com/problems/multi-source-flood-fill/

#include <stdlib.h>
#include <string.h>

int** colorGrid(int n, int m, int** sources, int sourcesSize, int* sourcesColSize, int* returnSize, int** returnColumnSizes) {
    (void)sourcesColSize;
    int** ans = malloc((size_t)n * sizeof(int*));
    for (int i = 0; i < n; i++) ans[i] = calloc((size_t)m, sizeof(int));
    int* q = malloc((size_t)(n * m * 3 + 16) * sizeof(int));
    int qn = 0;
    for (int i = 0; i < sourcesSize; i++) {
        q[qn++] = sources[i][0];
        q[qn++] = sources[i][1];
        q[qn++] = sources[i][2];
        ans[sources[i][0]][sources[i][1]] = sources[i][2];
    }
    int dirs[5] = {-1, 0, 1, 0, -1};
    while (qn > 0) {
        int* vis = calloc((size_t)(n * m), sizeof(int));
        int* next = malloc((size_t)(n * m * 3 + 16) * sizeof(int));
        int nn = 0;
        for (int i = 0; i < qn; i += 3) {
            int r = q[i], c = q[i + 1], color = q[i + 2];
            for (int d = 0; d < 4; d++) {
                int x = r + dirs[d], y = c + dirs[d + 1];
                if (x >= 0 && x < n && y >= 0 && y < m && ans[x][y] == 0) {
                    int id = x * m + y;
                    if (color > vis[id]) vis[id] = color;
                }
            }
        }
        for (int x = 0; x < n; x++) {
            for (int y = 0; y < m; y++) {
                int id = x * m + y;
                if (vis[id]) {
                    ans[x][y] = vis[id];
                    next[nn++] = x; next[nn++] = y; next[nn++] = vis[id];
                }
            }
        }
        free(vis); free(q);
        q = next; qn = nn;
    }
    free(q);
    *returnSize = n;
    *returnColumnSizes = malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) (*returnColumnSizes)[i] = m;
    return ans;
}
