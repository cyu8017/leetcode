// LeetCode 2536 - Increment Submatrices by One
// https://leetcode.com/problems/increment-submatrices-by-one/

public class Solution {
    public int[][] RangeAddQueries(int n, int[][] queries) {
        int[][] diff = new int[n + 1][];
        for (int i = 0; i <= n; i++) diff[i] = new int[n + 1];
        foreach (var q in queries) {
            int r1 = q[0], c1 = q[1], r2 = q[2], c2 = q[3];
            diff[r1][c1]++;
            diff[r1][c2 + 1]--;
            diff[r2 + 1][c1]--;
            diff[r2 + 1][c2 + 1]++;
        }
        int[][] mat = new int[n][];
        for (int i = 0; i < n; i++) {
            mat[i] = new int[n];
            for (int j = 0; j < n; j++) {
                int v = diff[i][j];
                if (i > 0) v += mat[i - 1][j];
                if (j > 0) v += mat[i][j - 1];
                if (i > 0 && j > 0) v -= mat[i - 1][j - 1];
                mat[i][j] = v;
            }
        }
        return mat;
    }
}
