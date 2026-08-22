// LeetCode 2387 - Median of a Row Wise Sorted Matrix
// https://leetcode.com/problems/median-of-a-row-wise-sorted-matrix/

int matrixMedian(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    int lo = 1, hi = 1000000, need = (m * n) / 2 + 1;
    while (lo < hi) {
        int mid = (lo + hi) / 2, cnt = 0;
        for (int i = 0; i < m; i++) {
            int l = 0, r = n;
            while (l < r) {
                int m2 = (l + r) / 2;
                if (grid[i][m2] <= mid) l = m2 + 1;
                else r = m2;
            }
            cnt += l;
        }
        if (cnt >= need) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
