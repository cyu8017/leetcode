// LeetCode 1605 - Find Valid Matrix Given Row and Column Sums
// https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/

using System;

public class Solution {
    public int[][] RestoreMatrix(int[] rowSum, int[] colSum) {
        int m = rowSum.Length, n = colSum.Length;
        var ans = new int[m][];
        for (int r = 0; r < m; r++) ans[r] = new int[n];
        int i = 0, j = 0;
        while (i < m && j < n) {
            int x = Math.Min(rowSum[i], colSum[j]);
            ans[i][j] = x;
            rowSum[i] -= x;
            colSum[j] -= x;
            if (rowSum[i] == 0) i++;
            if (colSum[j] == 0) j++;
        }
        return ans;
    }
}
