// LeetCode 3565 - Sequential Grid Path Cover
// https://leetcode.com/problems/sequential-grid-path-cover/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

static int m_g, n_g, **grid_g, path_len;
static int path_buf[400][2];
static unsigned long long st;
static int dirs[5] = {-1, 0, 1, 0, -1};

static int fidx(int i, int j) { return i * n_g + j; }

static bool dfs(int i, int j, int v) {
    path_buf[path_len][0] = i;
    path_buf[path_len][1] = j;
    path_len++;
    if (path_len == m_g * n_g) return true;
    int idx = fidx(i, j);
    st |= 1ULL << idx;
    if (grid_g[i][j] == v) v++;
    for (int t = 0; t < 4; t++) {
        int x = i + dirs[t], y = j + dirs[t + 1];
        if (0 <= x && x < m_g && 0 <= y && y < n_g) {
            int idx2 = fidx(x, y);
            if (((st >> idx2) & 1ULL) == 0 && (grid_g[x][y] == 0 || grid_g[x][y] == v)) {
                if (dfs(x, y, v)) return true;
            }
        }
    }
    path_len--;
    st ^= 1ULL << idx;
    return false;
}

int** findPath(int** grid, int gridSize, int* gridColSize, int k, int* returnSize, int** returnColumnSizes) {
    (void)k;
    m_g = gridSize; n_g = gridColSize[0]; grid_g = grid;
    for (int i = 0; i < m_g; i++) {
        for (int j = 0; j < n_g; j++) {
            if (grid[i][j] == 0 || grid[i][j] == 1) {
                path_len = 0; st = 0;
                if (dfs(i, j, 1)) {
                    int** ans = (int**)malloc((size_t)path_len * sizeof(int*));
                    *returnColumnSizes = (int*)malloc((size_t)path_len * sizeof(int));
                    for (int t = 0; t < path_len; t++) {
                        ans[t] = (int*)malloc(2 * sizeof(int));
                        ans[t][0] = path_buf[t][0];
                        ans[t][1] = path_buf[t][1];
                        (*returnColumnSizes)[t] = 2;
                    }
                    *returnSize = path_len;
                    return ans;
                }
            }
        }
    }
    *returnSize = 0;
    *returnColumnSizes = NULL;
    return NULL;
}
