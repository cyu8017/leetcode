// LeetCode 3552 - Grid Teleportation Traversal
// https://leetcode.com/problems/grid-teleportation-traversal/

#include <ctype.h>
#include <stdlib.h>
#include <string.h>

#define INF3552 (1 << 30)

int minMoves(char** matrix, int matrixSize) {
    int m = matrixSize, n = (int)strlen(matrix[0]);
    int portals[26][200];
    int pcnt[26] = {0};
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++) {
            char c = matrix[i][j];
            if (c >= 'A' && c <= 'Z') {
                int idx = c - 'A';
                portals[idx][pcnt[idx]++] = i * n + j;
            }
        }
    int usedPortal[26] = {0};
    int** dist = (int**)malloc((size_t)m * sizeof(int*));
    for (int i = 0; i < m; i++) {
        dist[i] = (int*)malloc((size_t)n * sizeof(int));
        for (int j = 0; j < n; j++) dist[i][j] = INF3552;
    }
    dist[0][0] = 0;
    int* dq = (int*)malloc((size_t)(m * n * 4 + 10) * sizeof(int));
    int head = m * n, tail = m * n;
    dq[tail++] = 0;
    int dirs[5] = {-1, 0, 1, 0, -1};
    while (head < tail) {
        int cur = dq[head++];
        int i = cur / n, j = cur % n;
        int d = dist[i][j];
        if (i == m - 1 && j == n - 1) {
            for (int x = 0; x < m; x++) free(dist[x]);
            free(dist); free(dq);
            return d;
        }
        char c = matrix[i][j];
        if (c >= 'A' && c <= 'Z' && !usedPortal[c - 'A']) {
            int idx = c - 'A';
            usedPortal[idx] = 1;
            for (int t = 0; t < pcnt[idx]; t++) {
                int pos = portals[idx][t];
                int x = pos / n, y = pos % n;
                if (d < dist[x][y]) {
                    dist[x][y] = d;
                    dq[--head] = pos;
                }
            }
        }
        for (int di = 0; di < 4; di++) {
            int x = i + dirs[di], y = j + dirs[di + 1];
            if (x >= 0 && x < m && y >= 0 && y < n && matrix[x][y] != '#' && d + 1 < dist[x][y]) {
                dist[x][y] = d + 1;
                dq[tail++] = x * n + y;
            }
        }
    }
    for (int x = 0; x < m; x++) free(dist[x]);
    free(dist); free(dq);
    return -1;
}
