// LeetCode 3446 - Sort Matrix by Diagonals
// https://leetcode.com/problems/sort-matrix-by-diagonals/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> sortMatrix(std::vector<std::vector<int>>& grid) {
        int n = (int)grid.size();
        std::unordered_map<int, std::vector<int>> diags;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) diags[i - j].push_back(grid[i][j]);
        }
        for (auto& [k, arr] : diags) {
            if (k >= 0) std::sort(arr.begin(), arr.end(), std::greater<int>());
            else std::sort(arr.begin(), arr.end());
        }
        std::unordered_map<int, int> idx;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int k = i - j;
                grid[i][j] = diags[k][idx[k]++];
            }
        }
        return grid;
    }
};
