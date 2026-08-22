// LeetCode 3529 - Count Cells in Overlapping Horizontal and Vertical Substrings
// https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/

#include <stdlib.h>
#include <string.h>

int countCells(char** grid, int gridSize, int* gridColSize, char* pattern) {
    int m = gridSize, n = gridColSize[0];
    int plen = (int)strlen(pattern);
    char* row = (char*)malloc((size_t)(m * n));
    char* col = (char*)malloc((size_t)(m * n));
    int ri = 0, ci = 0;
    for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) row[ri++] = grid[i][j];
    for (int j = 0; j < n; j++) for (int i = 0; i < m; i++) col[ci++] = grid[i][j];
    char** hMark = (char**)malloc((size_t)m * sizeof(char*));
    char** vMark = (char**)malloc((size_t)m * sizeof(char*));
    for (int i = 0; i < m; i++) {
        hMark[i] = (char*)calloc((size_t)n, 1);
        vMark[i] = (char*)calloc((size_t)n, 1);
    }
    for (int i = 0; i + plen <= m * n; i++) {
        int ok = 1;
        for (int t = 0; t < plen; t++) if (row[i + t] != pattern[t]) { ok = 0; break; }
        if (ok) for (int t = 0; t < plen; t++) { int pos = i + t; hMark[pos / n][pos % n] = 1; }
    }
    for (int i = 0; i + plen <= m * n; i++) {
        int ok = 1;
        for (int t = 0; t < plen; t++) if (col[i + t] != pattern[t]) { ok = 0; break; }
        if (ok) for (int t = 0; t < plen; t++) { int pos = i + t; vMark[pos % m][pos / m] = 1; }
    }
    int ans = 0;
    for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) if (hMark[i][j] && vMark[i][j]) ans++;
    for (int i = 0; i < m; i++) { free(hMark[i]); free(vMark[i]); }
    free(hMark); free(vMark); free(row); free(col);
    return ans;
}
