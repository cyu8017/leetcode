// LeetCode 1886 - Determine Whether Matrix Can Be Obtained By Rotation
// https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

public class Solution {
    public bool FindRotation(int[][] mat, int[][] target) {
        int[][] current = mat;
        for (int r = 0; r < 4; r++) {
            if (Same(current, target)) {
                return true;
            }
            current = Rotate(current);
        }
        return false;
    }

    private static bool Same(int[][] a, int[][] b) {
        for (int i = 0; i < a.Length; i++) {
            for (int j = 0; j < a[i].Length; j++) {
                if (a[i][j] != b[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }

    private static int[][] Rotate(int[][] mat) {
        int n = mat.Length;
        var next = new int[n][];
        for (int i = 0; i < n; i++) {
            next[i] = new int[n];
            for (int j = 0; j < n; j++) {
                next[i][j] = mat[n - 1 - j][i];
            }
        }
        return next;
    }
}
