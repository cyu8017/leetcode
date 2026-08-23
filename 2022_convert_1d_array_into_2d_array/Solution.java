// LeetCode 2022 - Convert 1D Array Into 2D Array
// https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution {
    public int[][] construct2DArray(int[] original, int m, int n) {
        if (original.length != m * n) return new int[0][];
        int[][] ans = new int[m][n];
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) ans[i][j] = original[i * n + j];
        return ans;
    }
}
