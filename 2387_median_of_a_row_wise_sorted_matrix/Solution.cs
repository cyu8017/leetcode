// LeetCode 2387 - Median of a Row Wise Sorted Matrix
// https://leetcode.com/problems/median-of-a-row-wise-sorted-matrix/

public class Solution {
    public int MatrixMedian(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        int lo = 1, hi = 1000000;
        int need = (m * n) / 2 + 1;
        int CountLE(int x) {
            int cnt = 0;
            foreach (var row in grid) {
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
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (CountLE(mid) >= need) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}
