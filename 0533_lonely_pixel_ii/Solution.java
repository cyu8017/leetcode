// LeetCode 0533 - Lonely Pixel II
// https://leetcode.com/problems/lonely-pixel-ii/

public class Solution {
    public int findBlackPixel(Object[] picture, int target) {
        int rows = picture.length;
        int cols = ((String[]) picture[0]).length;
        String[] rowStrings = new String[rows];
        int[] rowCounts = new int[rows];
        int[] colCounts = new int[cols];

        for (int r = 0; r < rows; r++) {
            String[] row = (String[]) picture[r];
            StringBuilder builder = new StringBuilder();
            for (int c = 0; c < cols; c++) {
                builder.append(row[c]);
                if ("B".equals(row[c])) {
                    rowCounts[r]++;
                    colCounts[c]++;
                }
            }
            rowStrings[r] = builder.toString();
        }

        int lonely = 0;
        for (int r = 0; r < rows; r++) {
            if (rowCounts[r] != target) {
                continue;
            }
            String[] row = (String[]) picture[r];
            for (int c = 0; c < cols; c++) {
                if (!"B".equals(row[c]) || colCounts[c] != target) {
                    continue;
                }
                boolean matches = true;
                for (int i = 0; i < rows; i++) {
                    if ("B".equals(((String[]) picture[i])[c]) && !rowStrings[r].equals(rowStrings[i])) {
                        matches = false;
                        break;
                    }
                }
                if (matches) {
                    lonely++;
                }
            }
        }
        return lonely;
    }
}
