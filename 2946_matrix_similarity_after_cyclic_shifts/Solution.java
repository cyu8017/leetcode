// LeetCode 2946 - Matrix Similarity After Cyclic Shifts
// https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/

class Solution {
    public boolean areSimilar(int[][] mat, int k) {
        int m = mat.length, n = mat[0].length;
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
