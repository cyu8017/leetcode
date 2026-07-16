// LeetCode 0048 - Rotate Image
// https://leetcode.com/problems/rotate-image/

public class Solution {
    public void Rotate(int[][] matrix) {
        int n = matrix.Length;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                (matrix[i][j], matrix[j][i]) = (matrix[j][i], matrix[i][j]);
            }
        }

        for (int i = 0; i < n; i++) {
            Array.Reverse(matrix[i]);
        }
    }
}
