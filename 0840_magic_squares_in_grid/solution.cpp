// LeetCode 0840 - Magic Squares In Grid
// https://leetcode.com/problems/magic-squares-in-grid/

#include <algorithm>
#include <vector>

class Solution {
public:
    int numMagicSquaresInside(std::vector<std::vector<int>>& grid) {
        int rows = static_cast<int>(grid.size());
        int cols = static_cast<int>(grid[0].size());
        if (rows < 3 || cols < 3) {
            return 0;
        }
        auto magic = [&](int r, int c) {
            std::vector<int> vals;
            for (int i = 0; i < 3; ++i) {
                for (int j = 0; j < 3; ++j) {
                    vals.push_back(grid[r + i][c + j]);
                }
            }
            std::sort(vals.begin(), vals.end());
            for (int i = 0; i < 9; ++i) {
                if (vals[i] != i + 1) {
                    return false;
                }
            }
            auto& a = grid;
            return a[r][c] + a[r][c + 1] + a[r][c + 2] == 15 &&
                   a[r + 1][c] + a[r + 1][c + 1] + a[r + 1][c + 2] == 15 &&
                   a[r + 2][c] + a[r + 2][c + 1] + a[r + 2][c + 2] == 15 &&
                   a[r][c] + a[r + 1][c] + a[r + 2][c] == 15 &&
                   a[r][c + 1] + a[r + 1][c + 1] + a[r + 2][c + 1] == 15 &&
                   a[r][c + 2] + a[r + 1][c + 2] + a[r + 2][c + 2] == 15 &&
                   a[r][c] + a[r + 1][c + 1] + a[r + 2][c + 2] == 15 &&
                   a[r][c + 2] + a[r + 1][c + 1] + a[r + 2][c] == 15;
        };
        int ans = 0;
        for (int i = 0; i < rows - 2; ++i) {
            for (int j = 0; j < cols - 2; ++j) {
                if (magic(i, j)) {
                    ++ans;
                }
            }
        }
        return ans;
    }
};
