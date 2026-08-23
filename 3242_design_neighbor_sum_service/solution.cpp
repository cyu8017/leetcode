// LeetCode 3242 - Design Neighbor Sum Service
// https://leetcode.com/problems/design-neighbor-sum-service/

#include <unordered_map>
#include <utility>
#include <vector>

class NeighborSum {
    std::vector<std::vector<int>> grid;
    std::unordered_map<int, std::pair<int, int>> d;
    int dirs[2][5] = {{-1, 0, 1, 0, -1}, {-1, 1, 1, -1, -1}};

    int cal(int value, int k) {
        auto p = d[value];
        int s = 0;
        for (int q = 0; q < 4; q++) {
            int x = p.first + dirs[k][q], y = p.second + dirs[k][q + 1];
            if (x >= 0 && x < (int)grid.size() && y >= 0 && y < (int)grid[0].size()) {
                s += grid[x][y];
            }
        }
        return s;
    }

public:
    NeighborSum(std::vector<std::vector<int>>& grid_) : grid(grid_) {
        for (int i = 0; i < (int)grid.size(); i++) {
            for (int j = 0; j < (int)grid[i].size(); j++) {
                d[grid[i][j]] = {i, j};
            }
        }
    }

    int adjacentSum(int value) { return cal(value, 0); }

    int diagonalSum(int value) { return cal(value, 1); }
};
