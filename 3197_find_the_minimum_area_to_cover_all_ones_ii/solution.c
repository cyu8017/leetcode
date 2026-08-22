// LeetCode 3197 - Find the Minimum Area to Cover All Ones II
// https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/

#include <limits.h>

static int **g3197, m3197, n3197;

static int area3197(int i1, int j1, int i2, int j2) {
    int x1 = INT_MAX, y1 = INT_MAX, x2 = INT_MIN, y2 = INT_MIN;
    for (int i = i1; i <= i2; i++)
        for (int j = j1; j <= j2; j++)
            if (g3197[i][j] == 1) {
                if (i < x1) x1 = i; if (j < y1) y1 = j;
                if (i > x2) x2 = i; if (j > y2) y2 = j;
            }
    if (x1 == INT_MAX) return 0;
    return (x2 - x1 + 1) * (y2 - y1 + 1);
}
static int min3(int a, int b) { return a < b ? a : b; }

int minimumSum(int** grid, int gridSize, int* gridColSize) {
    g3197 = grid; m3197 = gridSize; n3197 = gridColSize[0];
    int ans = m3197 * n3197;
    for (int i1 = 0; i1 < m3197 - 1; i1++)
        for (int i2 = i1 + 1; i2 < m3197 - 1; i2++)
            ans = min3(ans, area3197(0, 0, i1, n3197 - 1) + area3197(i1 + 1, 0, i2, n3197 - 1) + area3197(i2 + 1, 0, m3197 - 1, n3197 - 1));
    for (int j1 = 0; j1 < n3197 - 1; j1++)
        for (int j2 = j1 + 1; j2 < n3197 - 1; j2++)
            ans = min3(ans, area3197(0, 0, m3197 - 1, j1) + area3197(0, j1 + 1, m3197 - 1, j2) + area3197(0, j2 + 1, m3197 - 1, n3197 - 1));
    for (int i = 0; i < m3197 - 1; i++)
        for (int j = 0; j < n3197 - 1; j++) {
            ans = min3(ans, area3197(0, 0, i, j) + area3197(0, j + 1, i, n3197 - 1) + area3197(i + 1, 0, m3197 - 1, n3197 - 1));
            ans = min3(ans, area3197(0, 0, i, n3197 - 1) + area3197(i + 1, 0, m3197 - 1, j) + area3197(i + 1, j + 1, m3197 - 1, n3197 - 1));
            ans = min3(ans, area3197(0, 0, i, j) + area3197(i + 1, 0, m3197 - 1, j) + area3197(0, j + 1, m3197 - 1, n3197 - 1));
            ans = min3(ans, area3197(0, 0, m3197 - 1, j) + area3197(0, j + 1, i, n3197 - 1) + area3197(i + 1, j + 1, m3197 - 1, n3197 - 1));
        }
    return ans;
}
