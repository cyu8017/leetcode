// LeetCode 1861 - Rotating the Box
// https://leetcode.com/problems/rotating-the-box/

public class Solution {
    public char[][] RotateTheBox(char[][] boxGrid) {
        int m = boxGrid.Length;
        int n = boxGrid[0].Length;
        var rotated = new char[n][];
        for (int i = 0; i < n; i++) {
            rotated[i] = new char[m];
            for (int j = 0; j < m; j++) {
                rotated[i][j] = '.';
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                rotated[i][j] = boxGrid[m - 1 - j][i];
            }
        }
        for (int col = 0; col < m; col++) {
            int row = n - 1;
            for (int i = n - 1; i >= 0; i--) {
                if (rotated[i][col] == '*') {
                    row = i - 1;
                } else if (rotated[i][col] == '#') {
                    rotated[i][col] = '.';
                    rotated[row][col] = '#';
                    row--;
                }
            }
        }
        return rotated;
    }
}
