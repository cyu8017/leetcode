// LeetCode 1314 - Matrix Block Sum
// https://leetcode.com/problems/matrix-block-sum/

public class Solution {
    public int[][] MatrixBlockSum(int[][] mat, int k) {
        int m = mat.Length, n = mat[0].Length;
        var prefix = new int[m + 1, n + 1];
        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++)
                prefix[r + 1, c + 1] = mat[r][c] + prefix[r, c + 1] + prefix[r + 1, c] - prefix[r, c];
        var answer = new int[m][];
        for (int r = 0; r < m; r++) {
            answer[r] = new int[n];
            for (int c = 0; c < n; c++) {
                int r1 = System.Math.Max(0, r - k), c1 = System.Math.Max(0, c - k);
                int r2 = System.Math.Min(m, r + k + 1), c2 = System.Math.Min(n, c + k + 1);
                answer[r][c] = prefix[r2, c2] - prefix[r1, c2] - prefix[r2, c1] + prefix[r1, c1];
            }
        }
        return answer;
    }
}
