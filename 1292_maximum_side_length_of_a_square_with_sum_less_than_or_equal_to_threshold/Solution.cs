// LeetCode 1292 - Maximum Side Length of a Square with Sum Less than or Equal to Threshold
// https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

public class Solution {
    public int MaxSideLength(int[][] mat, int threshold) {
        int m = mat.Length, n = mat[0].Length;
        var prefix = new int[m + 1][];
        for (int i = 0; i <= m; i++) prefix[i] = new int[n + 1];
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                prefix[r + 1][c + 1] = mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c];
            }
        }
        bool Possible(int size) {
            for (int r = size; r <= m; r++) {
                for (int c = size; c <= n; c++) {
                    int sum = prefix[r][c] - prefix[r - size][c] - prefix[r][c - size] + prefix[r - size][c - size];
                    if (sum <= threshold) return true;
                }
            }
            return false;
        }
        int lo = 0, hi = System.Math.Min(m, n);
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (Possible(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
}
