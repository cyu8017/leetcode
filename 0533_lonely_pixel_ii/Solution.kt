// LeetCode 0533 - Lonely Pixel II
// https://leetcode.com/problems/lonely-pixel-ii/

public class Solution {
    public int FindBlackPixel(string[][] picture, int target) {
        int rows = picture.Length;
        int cols = picture[0].Length;
        string[] rowStrings = new string[rows];
        int[] rowCounts = new int[rows];
        int[] colCounts = new int[cols];

        for (int r = 0; r < rows; r++) {
            rowStrings[r] = string.Concat(picture[r]);
            for (int c = 0; c < cols; c++) {
                if (picture[r][c] == "B") {
                    rowCounts[r]++;
                    colCounts[c]++;
                }
            }
        }

        int lonely = 0;
        for (int r = 0; r < rows; r++) {
            if (rowCounts[r] != target) {
                continue;
            }
            for (int c = 0; c < cols; c++) {
                if (picture[r][c] != "B" || colCounts[c] != target) {
                    continue;
                }
                bool matches = true;
                for (int i = 0; i < rows; i++) {
                    if (picture[i][c] == "B" && rowStrings[r] != rowStrings[i]) {
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
