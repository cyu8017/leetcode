// LeetCode 2852 - Sum of Remoteness of All Cells
// https://leetcode.com/problems/sum-of-remoteness-of-all-cells/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

long long sumRemoteness(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    bool** seen = (bool**)malloc(m * sizeof(bool*));
    for (int i = 0; i < m; i++) seen[i] = (bool*)calloc(n, sizeof(bool));
    long long total = 0;
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            if (grid[i][j] != -1) total += grid[i][j];
    int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
    long long ans = 0;
    int* qx = (int*)malloc(m * n * sizeof(int));
    int* qy = (int*)malloc(m * n * sizeof(int));
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == -1 || seen[i][j]) continue;
            int qh = 0, qt = 0;
            qx[qt] = i; qy[qt] = j; qt++;
            seen[i][j] = true;
            long long sum = 0;
            int cnt = 0;
            while (qh < qt) {
                int x = qx[qh], y = qy[qh]; qh++;
                sum += grid[x][y];
                cnt++;
                for (int d = 0; d < 4; d++) {
                    int ni = x + dirs[d][0], nj = y + dirs[d][1];
                    if (ni >= 0 && nj >= 0 && ni < m && nj < n && !seen[ni][nj] && grid[ni][nj] != -1) {
                        seen[ni][nj] = true;
                        qx[qt] = ni; qy[qt] = nj; qt++;
                    }
                }
            }
            ans += (total - sum) * cnt;
        }
    }
    for (int i = 0; i < m; i++) free(seen[i]);
    free(seen); free(qx); free(qy);
    return ans;
}
