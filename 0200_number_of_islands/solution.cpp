// LeetCode 0200 - Number of Islands
// https://leetcode.com/problems/number-of-islands/

#include <vector>

class Solution {
    void flood(std::vector<std::vector<char>>& grid, int row, int col) {
        if (row < 0 || col < 0 || row >= static_cast<int>(grid.size()) ||
            col >= static_cast<int>(grid[0].size()) || grid[row][col] != '1') {
            return;
        }
        grid[row][col] = '0';
        flood(grid, row + 1, col);
        flood(grid, row - 1, col);
        flood(grid, row, col + 1);
        flood(grid, row, col - 1);
    }

public:
    int numIslands(std::vector<std::vector<char>>& grid) {
        if (grid.empty() || grid[0].empty()) {
            return 0;
        }
        int islands = 0;
        for (int row = 0; row < static_cast<int>(grid.size()); ++row) {
            for (int col = 0; col < static_cast<int>(grid[row].size()); ++col) {
                if (grid[row][col] == '1') {
                    ++islands;
                    flood(grid, row, col);
                }
            }
        }
        return islands;
    }
};
