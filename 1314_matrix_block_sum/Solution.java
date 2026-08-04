// LeetCode 1314 - Matrix Block Sum
// https://leetcode.com/problems/matrix-block-sum/

class Solution {
    public int[][] matrixBlockSum(int[][] mat, int k) {
        int m = mat.length, n = mat[0].length;
        int[][] prefix = new int[m + 1][n + 1];
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                prefix[r + 1][c + 1] = mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c];
            }
        }
        int[][] answer = new int[m][n];
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                int r1 = Math.max(0, r - k), c1 = Math.max(0, c - k);
                int r2 = Math.min(m, r + k + 1), c2 = Math.min(n, c + k + 1);
                answer[r][c] = prefix[r2][c2] - prefix[r1][c2] - prefix[r2][c1] + prefix[r1][c1];
            }
        }
        return answer;
    }
}
