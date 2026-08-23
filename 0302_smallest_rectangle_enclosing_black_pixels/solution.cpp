// LeetCode 0302 - Smallest Rectangle Enclosing Black Pixels
// https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/

#include <string>
#include <vector>

class Solution {
public:
    int minArea(std::vector<std::vector<std::string>>& image, int x, int y) {
        int rows = static_cast<int>(image.size());
        int cols = static_cast<int>(image[0].size());

        auto columnHasBlack = [&](int col) {
            for (int row = 0; row < rows; row++) {
                if (image[row][col] == "1") {
                    return true;
                }
            }
            return false;
        };

        auto rowHasBlack = [&](int row) {
            for (int col = 0; col < cols; col++) {
                if (image[row][col] == "1") {
                    return true;
                }
            }
            return false;
        };

        int left = 0;
        int right = y;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (columnHasBlack(mid)) {
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
            if (columnHasBlack(mid)) {
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
            if (rowHasBlack(mid)) {
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
            if (rowHasBlack(mid)) {
                top = mid;
            } else {
                bottom = mid - 1;
            }
        }
        int bottomBound = top;

        return (rightBound - leftBound + 1) * (bottomBound - topBound + 1);
    }
};
