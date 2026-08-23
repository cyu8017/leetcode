// LeetCode 2732 - Find a Good Subset of the Matrix
// https://leetcode.com/problems/find-a-good-subset-of-the-matrix/

#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> goodSubsetofBinaryMatrix(std::vector<std::vector<int>>& grid) {
        int n = (int)grid[0].size();
        std::unordered_map<int, int> first;
        for (int i = 0; i < (int)grid.size(); i++) {
            int mask = 0;
            for (int j = 0; j < n; j++) if (grid[i][j] == 1) mask |= 1 << j;
            if (mask == 0) return {i};
            for (auto& [m, idx] : first) {
                if ((m & mask) == 0) {
                    if (idx < i) return {idx, i};
                    return {i, idx};
                }
            }
            if (!first.count(mask)) first[mask] = i;
        }
        return {};
    }
};
