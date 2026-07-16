// LeetCode 0361 - Bomb Enemy
// https://leetcode.com/problems/bomb-enemy/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int maxKilledEnemies(std::vector<std::vector<char>>& grid) {
        if (grid.empty() || grid[0].empty()) {
            return 0;
        }

        int rows = static_cast<int>(grid.size());
        int cols = static_cast<int>(grid[0].size());
        std::vector<std::vector<int>> rowHits(rows, std::vector<int>(cols, 0));
        std::vector<std::vector<int>> colHits(rows, std::vector<int>(cols, 0));

        for (int row = 0; row < rows; ++row) {
            int count = 0;
            for (int col = 0; col < cols; ++col) {
                if (grid[row][col] == 'W') {
                    count = 0;
                } else if (grid[row][col] == 'E') {
                    count += 1;
                } else {
                    rowHits[row][col] = count;
                }
            }
            count = 0;
            for (int col = cols - 1; col >= 0; --col) {
                if (grid[row][col] == 'W') {
                    count = 0;
                } else if (grid[row][col] == 'E') {
                    count += 1;
                } else {
                    rowHits[row][col] += count;
                }
            }
        }

        for (int col = 0; col < cols; ++col) {
            int count = 0;
            for (int row = 0; row < rows; ++row) {
                if (grid[row][col] == 'W') {
                    count = 0;
                } else if (grid[row][col] == 'E') {
                    count += 1;
                } else {
                    colHits[row][col] = count;
                }
            }
            count = 0;
            for (int row = rows - 1; row >= 0; --row) {
                if (grid[row][col] == 'W') {
                    count = 0;
                } else if (grid[row][col] == 'E') {
                    count += 1;
                } else {
                    colHits[row][col] += count;
                }
            }
        }

        int result = 0;
        for (int row = 0; row < rows; ++row) {
            for (int col = 0; col < cols; ++col) {
                result = std::max(result, rowHits[row][col] + colHits[row][col]);
            }
        }

        return result;
    }
};
