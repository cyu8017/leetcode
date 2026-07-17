// LeetCode 1886 - Determine Whether Matrix Can Be Obtained By Rotation
// https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

import java.util.Arrays;

class Solution {
    public boolean findRotation(int[][] mat, int[][] target) {
        int n = mat.length;
        int[][] current = mat;
        for (int rotation = 0; rotation < 4; rotation++) {
            if (equalsMatrix(current, target)) {
                return true;
            }
            int[][] rotated = new int[n][n];
            for (int col = 0; col < n; col++) {
                for (int row = 0; row < n; row++) {
                    rotated[col][row] = current[n - 1 - row][col];
                }
            }
            current = rotated;
        }
        return false;
    }

    private boolean equalsMatrix(int[][] left, int[][] right) {
        for (int i = 0; i < left.length; i++) {
            if (!Arrays.equals(left[i], right[i])) {
                return false;
            }
        }
        return true;
    }
}
