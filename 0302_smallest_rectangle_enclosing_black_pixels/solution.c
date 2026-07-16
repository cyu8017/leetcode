// LeetCode 0302 - Smallest Rectangle Enclosing Black Pixels
// https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/

#include <stdbool.h>
#include <string.h>

static bool columnHasBlack(char** image, int rows, int col) {
    for (int row = 0; row < rows; row++) {
        if (image[row][col] == '1') {
            return true;
        }
    }
    return false;
}

static bool rowHasBlack(char** image, int cols, int row) {
    for (int col = 0; col < cols; col++) {
        if (image[row][col] == '1') {
            return true;
        }
    }
    return false;
}

int minArea(char** image, int imageSize, int* imageColSize, int x, int y) {
    int rows = imageSize;
    int cols = imageColSize[0];

    int left = 0;
    int right = y;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (columnHasBlack(image, rows, mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    int leftBound = left;

    left = y;
    right = cols - 1;
    while (left < right) {
        int mid = left + (right - left + 1) / 2;
        if (columnHasBlack(image, rows, mid)) {
            left = mid;
        } else {
            right = mid - 1;
        }
    }
    int rightBound = left;

    int top = 0;
    int bottom = x;
    while (top < bottom) {
        int mid = top + (bottom - top) / 2;
        if (rowHasBlack(image, cols, mid)) {
            bottom = mid;
        } else {
            top = mid + 1;
        }
    }
    int topBound = top;

    top = x;
    bottom = rows - 1;
    while (top < bottom) {
        int mid = top + (bottom - top + 1) / 2;
        if (rowHasBlack(image, cols, mid)) {
            top = mid;
        } else {
            bottom = mid - 1;
        }
    }
    int bottomBound = top;

    return (rightBound - leftBound + 1) * (bottomBound - topBound + 1);
}
