// LeetCode 1260 - Shift 2D Grid
// https://leetcode.com/problems/shift-2d-grid/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> shiftGrid(std::vector<std::vector<int>>& grid, int k) {
        const int m = static_cast<int>(grid.size());
        const int n = static_cast<int>(grid[0].size());
        std::vector<int> flat;
        flat.reserve(m * n);
        for (const auto& row : grid) {
            for (int x : row) {
                flat.push_back(x);
            }
        }
        const int total = m * n;
        k %= total;
        if (k) {
            std::vector<int> rotated;
            rotated.insert(rotated.end(), flat.end() - k, flat.end());
            rotated.insert(rotated.end(), flat.begin(), flat.end() - k);
            flat.swap(rotated);
        }
        std::vector<std::vector<int>> answer(m, std::vector<int>(n));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                answer[i][j] = flat[i * n + j];
            }
        }
        return answer;
    }
};
