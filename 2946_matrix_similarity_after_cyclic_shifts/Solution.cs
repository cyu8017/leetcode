// LeetCode 2946 - Matrix Similarity After Cyclic Shifts
// https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/

public class Solution {
    public bool AreSimilar(int[][] mat, int k) {
        int m = mat.Length, n = mat[0].Length;
        for (int i = 0; i < m; i++) {
            int shift;
            if (i % 2 == 0) {
                shift = n - (k % n);
                if (shift == n) shift = 0;
            } else {
                shift = k % n;
            }
            for (int j = 0; j < n; j++)
                if (mat[i][j] != mat[i][(j + shift) % n]) return false;
        }
        return true;
    }
}
