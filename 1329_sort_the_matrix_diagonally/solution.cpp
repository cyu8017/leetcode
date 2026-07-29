#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> diagonalSort(std::vector<std::vector<int>>& mat) {
        std::unordered_map<int, std::vector<int>> diagonals;
        int m = (int)mat.size(), n = (int)mat[0].size();
        for (int r = 0; r < m; ++r)
            for (int c = 0; c < n; ++c)
                diagonals[r - c].push_back(mat[r][c]);
        for (auto& [_, values] : diagonals)
            std::sort(values.begin(), values.end(), std::greater<int>());
        for (int r = 0; r < m; ++r)
            for (int c = 0; c < n; ++c) {
                mat[r][c] = diagonals[r - c].back();
                diagonals[r - c].pop_back();
            }
        return mat;
    }
};
