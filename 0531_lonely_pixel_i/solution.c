// LeetCode 0531 - Lonely Pixel I
// https://leetcode.com/problems/lonely-pixel-i/

int findLonelyPixel(char** picture, int pictureRowSize, int* pictureColSizes) {
    int lonely = 0;

    for (int r = 0; r < pictureRowSize; r++) {
        int rowCount = 0;
        for (int c = 0; c < pictureColSizes[r]; c++) {
            if (picture[r][c] == 'B') {
                rowCount++;
            }
        }

        for (int c = 0; c < pictureColSizes[r]; c++) {
            if (picture[r][c] != 'B' || rowCount != 1) {
                continue;
            }

            int colCount = 0;
            for (int row = 0; row < pictureRowSize; row++) {
                if (picture[row][c] == 'B') {
                    colCount++;
                }
            }

            if (colCount == 1) {
                lonely++;
            }
        }
    }

    return lonely;
}
