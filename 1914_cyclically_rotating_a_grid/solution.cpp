// LeetCode 1914 - Cyclically Rotating a Grid
// https://leetcode.com/problems/cyclically-rotating-a-grid/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> rotateGrid(std::vector<std::vector<int>>& grid, int k) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        int layers = std::min(m, n) / 2;
        for (int layer = 0; layer < layers; layer++) {
            std::vector<int> vals;
            for (int c = layer; c < n - layer; c++) vals.push_back(grid[layer][c]);
            for (int r = layer + 1; r < m - layer; r++) vals.push_back(grid[r][n - layer - 1]);
            if (m - 2 * layer > 1) {
                for (int c = n - layer - 2; c >= layer; c--) vals.push_back(grid[m - layer - 1][c]);
            }
            if (n - 2 * layer > 1) {
                for (int r = m - layer - 2; r > layer; r--) vals.push_back(grid[r][layer]);
            }
            int shift = k % (int)vals.size();
            std::rotate(vals.begin(), vals.begin() + shift, vals.end());
            int idx = 0;
            for (int c = layer; c < n - layer; c++) grid[layer][c] = vals[idx++];
            for (int r = layer + 1; r < m - layer; r++) grid[r][n - layer - 1] = vals[idx++];
            if (m - 2 * layer > 1) {
                for (int c = n - layer - 2; c >= layer; c--) grid[m - layer - 1][c] = vals[idx++];
            }
            if (n - 2 * layer > 1) {
                for (int r = m - layer - 2; r > layer; r--) grid[r][layer] = vals[idx++];
            }
        }
        return grid;
    }
};
