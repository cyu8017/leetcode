// LeetCode 2077 - Paths in Maze That Lead to Same Room
// https://leetcode.com/problems/paths-in-maze-that-lead-to-same-room/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int numberOfPaths(int n, int** corridors, int corridorsSize, int* corridorsColSize) {
    (void)corridorsColSize;
    bool** g = (bool**)malloc(((size_t)n + 1) * sizeof(bool*));
    for (int i = 0; i <= n; i++) g[i] = (bool*)calloc((size_t)n + 1, sizeof(bool));
    for (int i = 0; i < corridorsSize; i++) {
        int a = corridors[i][0], b = corridors[i][1];
        g[a][b] = g[b][a] = true;
    }
    int ans = 0;
    for (int i = 0; i < corridorsSize; i++) {
        int a = corridors[i][0], b = corridors[i][1];
        for (int c = 1; c <= n; c++) if (g[a][c] && g[b][c]) ans++;
    }
    for (int i = 0; i <= n; i++) free(g[i]);
    free(g);
    return ans / 3;
}
