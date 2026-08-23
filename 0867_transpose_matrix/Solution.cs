// LeetCode 0867 - Transpose Matrix
// https://leetcode.com/problems/transpose-matrix/

public class Solution {
    public int[][] Transpose(int[][] matrix) {
        int m = matrix.Length, n = matrix[0].Length;
        int[][] ans = new int[n][];
        for (int j = 0; j < n; j++) ans[j] = new int[m];
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                ans[j][i] = matrix[i][j];
        return ans;
    }
}
