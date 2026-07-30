// LeetCode 1582 - Special Positions in a Binary Matrix
// https://leetcode.com/problems/special-positions-in-a-binary-matrix/

public class Solution {
    public int NumSpecial(int[][] mat) {
        int m = mat.Length, n = mat[0].Length;
        int[] rows = new int[m], cols = new int[n];
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                rows[i] += mat[i][j];
                cols[j] += mat[i][j];
            }
        int ans = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (mat[i][j] == 1 && rows[i] == 1 && cols[j] == 1) ans++;
        return ans;
    }
}
