// LeetCode 2387 - Median of a Row Wise Sorted Matrix
// https://leetcode.com/problems/median-of-a-row-wise-sorted-matrix/

class Solution {
    public int matrixMedian(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int lo = 1, hi = 1_000_000;
        int need = (m * n) / 2 + 1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (countLE(grid, mid, n) >= need) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    private int countLE(int[][] grid, int x, int n) {
        int cnt = 0;
        for (int[] row : grid) {
            int l = 0, r = n;
            while (l < r) {
                int mid = (l + r) / 2;
                if (row[mid] <= x) l = mid + 1;
                else r = mid;
            }
            cnt += l;
        }
        return cnt;
    }
}
