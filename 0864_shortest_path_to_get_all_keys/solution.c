// LeetCode 0864 - Shortest Path to Get All Keys
// https://leetcode.com/problems/shortest-path-to-get-all-keys/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct { int r, c, mask, dist; } QNode;

int shortestPathAllKeys(char** grid, int gridSize) {
    int m = gridSize, n = (int)strlen(grid[0]);
    int all_keys = 0, sr = 0, sc = 0;
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++) {
            char ch = grid[i][j];
            if (ch == '@') { sr = i; sc = j; }
            else if (ch >= 'a' && ch <= 'f') all_keys |= 1 << (ch - 'a');
        }
    int masks = all_keys + 1;
    bool* seen = (bool*)calloc((size_t)m * n * masks, sizeof(bool));
    QNode* q = (QNode*)malloc((size_t)m * n * masks * sizeof(QNode));
    int qh = 0, qt = 0;
    q[qt++] = (QNode){sr, sc, 0, 0};
    seen[(sr * n + sc) * masks + 0] = true;
    int dr[4] = {1,-1,0,0}, dc[4] = {0,0,1,-1};
    while (qh < qt) {
        QNode cur = q[qh++];
        if (cur.mask == all_keys) {
            free(seen); free(q);
            return cur.dist;
        }
        for (int k = 0; k < 4; k++) {
            int nr = cur.r + dr[k], nc = cur.c + dc[k];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == '#') continue;
            char cell = grid[nr][nc];
            int nmask = cur.mask;
            if (cell >= 'a' && cell <= 'f') nmask |= 1 << (cell - 'a');
            if (cell >= 'A' && cell <= 'F' && !(cur.mask & (1 << (cell - 'A')))) continue;
            int sid = (nr * n + nc) * masks + nmask;
            if (!seen[sid]) {
                seen[sid] = true;
                q[qt++] = (QNode){nr, nc, nmask, cur.dist + 1};
            }
        }
    }
    free(seen); free(q);
    return -1;
}
