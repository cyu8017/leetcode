// LeetCode 0531 - Lonely Pixel I
// https://leetcode.com/problems/lonely-pixel-i/

public class Solution {
    public int FindLonelyPixel(char[][] picture) {
        int rows = picture.Length;
        int cols = picture[0].Length;
        int[] rowCounts = new int[rows];
        int[] colCounts = new int[cols];

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (picture[r][c] == 'B') {
                    rowCounts[r]++;
                    colCounts[c]++;
                }
            }
        }

        int lonely = 0;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (picture[r][c] == 'B' && rowCounts[r] == 1 && colCounts[c] == 1) {
                    lonely++;
                }
            }
        }
        return lonely;
    }
}
