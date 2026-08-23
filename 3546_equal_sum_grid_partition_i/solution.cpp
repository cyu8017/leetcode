// LeetCode 3546 - Equal Sum Grid Partition I
// https://leetcode.com/problems/equal-sum-grid-partition-i/

#include <vector>

class Solution {
public:
    bool canPartitionGrid(std::vector<std::vector<int>>& grid) {
        long long s = 0;
        for (auto& row : grid) for (int x : row) s += x;
        if (s % 2) return false;
        int m = (int)grid.size(), n = (int)grid[0].size();
        long long pre = 0;
        for (int i = 0; i < m; i++) {
            for (int x : grid[i]) pre += x;
            if (pre * 2 == s && i + 1 < m) return true;
        }
        pre = 0;
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < m; i++) pre += grid[i][j];
            if (pre * 2 == s && j + 1 < n) return true;
        }
        return false;
    }
};
