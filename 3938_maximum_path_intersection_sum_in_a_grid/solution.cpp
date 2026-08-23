// LeetCode 3938 - Maximum Path Intersection Sum in a Grid
// https://leetcode.com/problems/maximum-path-intersection-sum-in-a-grid/

#include <climits>
#include <functional>
#include <vector>

class Solution {
public:
    int maxPathSum(std::vector<std::vector<int>>& grid) {
        int rows = (int)grid.size(), cols = (int)grid[0].size();
        int answer = INT_MIN;
        auto checkLine = [&](int length, auto value) {
            int bestEnding = value(0) + value(1);
            if (bestEnding > answer) answer = bestEnding;
            for (int i = 2; i < length; i++) {
                if (value(i - 1) + value(i) > bestEnding + value(i)) bestEnding = value(i - 1) + value(i);
                else bestEnding += value(i);
                if (bestEnding > answer) answer = bestEnding;
            }
        };
        for (int row = 0; row < rows; row++) {
            checkLine(cols, [&](int col) { return grid[row][col]; });
        }
        for (int col = 0; col < cols; col++) {
            checkLine(rows, [&](int row) { return grid[row][col]; });
        }
        for (int row = 1; row + 1 < rows; row++) {
            for (int col = 1; col + 1 < cols; col++) {
                if (grid[row][col] > answer) answer = grid[row][col];
            }
        }
        return answer;
    }
};
