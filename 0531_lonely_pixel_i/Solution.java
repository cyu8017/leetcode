// LeetCode 0531 - Lonely Pixel I
// https://leetcode.com/problems/lonely-pixel-i/

public class Solution {
    public int findLonelyPixel(Object[] picture) {
        int rows = picture.length;
        int cols = ((String[]) picture[0]).length;
        int[] rowCounts = new int[rows];
        int[] colCounts = new int[cols];

        for (int r = 0; r < rows; r++) {
            String[] row = (String[]) picture[r];
            for (int c = 0; c < cols; c++) {
                if ("B".equals(row[c])) {
                    rowCounts[r]++;
                    colCounts[c]++;
                }
            }
        }

        int lonely = 0;
        for (int r = 0; r < rows; r++) {
            String[] row = (String[]) picture[r];
            for (int c = 0; c < cols; c++) {
                if ("B".equals(row[c]) && rowCounts[r] == 1 && colCounts[c] == 1) {
                    lonely++;
                }
            }
        }
        return lonely;
    }
}
