// LeetCode 0533 - Lonely Pixel II
// https://leetcode.com/problems/lonely-pixel-ii/

#include <string>
#include <vector>

class Solution {
public:
    int findBlackPixel(std::vector<std::vector<char>>& picture, int target) {
        const int rows = static_cast<int>(picture.size());
        const int cols = static_cast<int>(picture[0].size());
        std::vector<std::string> rowStrings(rows);
        std::vector<int> rowCounts(rows, 0);
        std::vector<int> colCounts(cols, 0);

        for (int r = 0; r < rows; ++r) {
            rowStrings[r].reserve(cols);
            for (int c = 0; c < cols; ++c) {
                rowStrings[r].push_back(picture[r][c]);
                if (picture[r][c] == 'B') {
                    ++rowCounts[r];
                    ++colCounts[c];
                }
            }
        }

        int lonely = 0;
        for (int r = 0; r < rows; ++r) {
            if (rowCounts[r] != target) {
                continue;
            }
            for (int c = 0; c < cols; ++c) {
                if (picture[r][c] != 'B' || colCounts[c] != target) {
                    continue;
                }
                bool matches = true;
                for (int i = 0; i < rows; ++i) {
                    if (picture[i][c] == 'B' && rowStrings[r] != rowStrings[i]) {
                        matches = false;
                        break;
                    }
                }
                if (matches) {
                    ++lonely;
                }
            }
        }
        return lonely;
    }
};
