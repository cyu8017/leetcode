// LeetCode 0302 - Smallest Rectangle Enclosing Black Pixels
// https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/

class Solution {
    public int minArea(char[][] image, int x, int y) {
        int rows = image.length;
        int cols = image[0].length;

        int leftBound = binarySearchLeft(image, y, rows);
        int rightBound = binarySearchRight(image, y, cols, rows);
        int topBound = binarySearchTop(image, x, cols);
        int bottomBound = binarySearchBottom(image, x, rows, cols);

        return (rightBound - leftBound + 1) * (bottomBound - topBound + 1);
    }

    private int binarySearchLeft(char[][] image, int y, int rows) {
        int left = 0;
        int right = y;
        while (left < right) {
            int mid = (left + right) / 2;
            if (columnHasBlack(image, mid, rows)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    private int binarySearchRight(char[][] image, int y, int cols, int rows) {
        int left = y;
        int right = cols - 1;
        while (left < right) {
            int mid = (left + right + 1) / 2;
            if (columnHasBlack(image, mid, rows)) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }

    private int binarySearchTop(char[][] image, int x, int cols) {
        int top = 0;
        int bottom = x;
        while (top < bottom) {
            int mid = (top + bottom) / 2;
            if (rowHasBlack(image, mid, cols)) {
                bottom = mid;
            } else {
                top = mid + 1;
            }
        }
        return top;
    }

    private int binarySearchBottom(char[][] image, int x, int rows, int cols) {
        int top = x;
        int bottom = rows - 1;
        while (top < bottom) {
            int mid = (top + bottom + 1) / 2;
            if (rowHasBlack(image, mid, cols)) {
                top = mid;
            } else {
                bottom = mid - 1;
            }
        }
        return top;
    }

    private boolean columnHasBlack(char[][] image, int col, int rows) {
        for (int row = 0; row < rows; row++) {
            if (image[row][col] == '1') {
                return true;
            }
        }
        return false;
    }

    private boolean rowHasBlack(char[][] image, int row, int cols) {
        for (int col = 0; col < cols; col++) {
            if (image[row][col] == '1') {
                return true;
            }
        }
        return false;
    }
}
