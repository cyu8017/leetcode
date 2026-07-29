// LeetCode 0959 - Regions Cut By Slashes
// https://leetcode.com/problems/regions-cut-by-slashes/

#include <stdlib.h>

static int find(int* p, int x) {
    while (p[x] != x) { p[x] = p[p[x]]; x = p[x]; }
    return x;
}

int regionsBySlashes(char** grid, int gridSize) {
    int n = gridSize;
    int N = n * n * 4;
    int* parent = (int*)malloc((size_t)N * sizeof(int));
    for (int i = 0; i < N; i++) parent[i] = i;
    for (int r = 0; r < n; r++) {
        for (int c = 0; c < n; c++) {
            int root = 4 * (r * n + c);
            char ch = grid[r][c];
            if (ch == '/') {
                parent[find(parent, root + 0)] = find(parent, root + 3);
                parent[find(parent, root + 1)] = find(parent, root + 2);
            } else if (ch == '\\') {
                parent[find(parent, root + 0)] = find(parent, root + 1);
                parent[find(parent, root + 2)] = find(parent, root + 3);
            } else {
                parent[find(parent, root + 0)] = find(parent, root + 1);
                parent[find(parent, root + 1)] = find(parent, root + 2);
                parent[find(parent, root + 2)] = find(parent, root + 3);
            }
            if (r + 1 < n) parent[find(parent, root + 2)] = find(parent, root + 4 * n + 0);
            if (c + 1 < n) parent[find(parent, root + 1)] = find(parent, root + 4 + 3);
        }
    }
    int ans = 0;
    for (int i = 0; i < N; i++) if (find(parent, i) == i) ans++;
    free(parent);
    return ans;
}
