// LeetCode 0533 - Lonely Pixel II
// https://leetcode.com/problems/lonely-pixel-ii/

#include <stdlib.h>
#include <string.h>

static int row_black_count(char** picture, int row, int cols) {
    int count = 0;
    for (int c = 0; c < cols; c++) {
        if (picture[row][c] == 'B') {
            count++;
        }
    }
    return count;
}

static int col_black_count(char** picture, int col, int rows) {
    int count = 0;
    for (int r = 0; r < rows; r++) {
        if (picture[r][col] == 'B') {
            count++;
        }
    }
    return count;
}

static int rows_match_in_column(char** picture, int anchorRow, int col, int rows, int cols) {
    for (int r = 0; r < rows; r++) {
        if (picture[r][col] != 'B') {
            continue;
        }
        if (memcmp(picture[anchorRow], picture[r], (size_t)cols) != 0) {
            return 0;
        }
    }
    return 1;
}

int findBlackPixel(char** picture, int pictureRowSize, int* pictureColSizes, int target) {
    const int cols = pictureColSizes[0];
    int lonely = 0;

    for (int r = 0; r < pictureRowSize; r++) {
        if (row_black_count(picture, r, cols) != target) {
            continue;
        }
        for (int c = 0; c < cols; c++) {
            if (picture[r][c] != 'B' || col_black_count(picture, c, pictureRowSize) != target) {
                continue;
            }
            if (rows_match_in_column(picture, r, c, pictureRowSize, cols)) {
                lonely++;
            }
        }
    }

    return lonely;
}
