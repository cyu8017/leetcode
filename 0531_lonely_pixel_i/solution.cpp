// LeetCode 0531 - Lonely Pixel I
// https://leetcode.com/problems/lonely-pixel-i/

#include <vector>

class Solution {
public:
    int findLonelyPixel(std::vector<std::vector<char>>& picture) {
        const int rows = static_cast<int>(picture.size());
        const int cols = static_cast<int>(picture[0].size());
        std::vector<int> rowCounts(rows, 0);
        std::vector<int> colCounts(cols, 0);

        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                if (picture[r][c] == 'B') {
                    ++rowCounts[r];
                    ++colCounts[c];
                }
            }
        }

        int lonely = 0;
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                if (picture[r][c] == 'B' && rowCounts[r] == 1 && colCounts[c] == 1) {
                    ++lonely;
                }
            }
        }
        return lonely;
    }
};
