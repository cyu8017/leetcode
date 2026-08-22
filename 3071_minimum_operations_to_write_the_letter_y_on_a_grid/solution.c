// LeetCode 3071 - Minimum Operations to Write the Letter Y on a Grid
// https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/

int minimumOperationsToWriteY(int** grid, int gridSize, int* gridColSize) {
    (void)gridColSize;
    int n = gridSize;
    int cnt1[3] = {0}, cnt2[3] = {0};
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int a = (i == j && i <= n / 2);
            int b = (i + j == n - 1 && i <= n / 2);
            int c = (j == n / 2 && i >= n / 2);
            if (a || b || c) cnt1[grid[i][j]]++;
            else cnt2[grid[i][j]]++;
        }
    }
    int ans = n * n;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (i != j) {
                int v = n * n - cnt1[i] - cnt2[j];
                if (v < ans) ans = v;
            }
        }
    }
    return ans;
}
