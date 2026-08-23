// LeetCode 2661 - First Completely Painted Row or Column
// https://leetcode.com/problems/first-completely-painted-row-or-column/

public class Solution {
    public int FirstCompleteIndex(int[] arr, int[][] mat) {
        int m = mat.Length, n = mat[0].Length;
        var pos = new (int r, int c)[m * n + 1];
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                pos[mat[i][j]] = (i, j);
        int[] rowCnt = new int[m], colCnt = new int[n];
        for (int i = 0; i < arr.Length; i++) {
            var (r, c) = pos[arr[i]];
            rowCnt[r]++; colCnt[c]++;
            if (rowCnt[r] == n || colCnt[c] == m) return i;
        }
        return -1;
    }
}
