// LeetCode 0407 - Trapping Rain Water II
// https://leetcode.com/problems/trapping-rain-water-ii/

#include <queue>
#include <tuple>
#include <vector>

class Solution {
public:
    int trapRainWater(vector<vector<int>>& heightMap) {
        if (heightMap.empty() || heightMap[0].empty()) {
            return 0;
        }

        int rows = static_cast<int>(heightMap.size());
        int cols = static_cast<int>(heightMap[0].size());
        if (rows < 3 || cols < 3) {
            return 0;
        }

        vector<vector<bool>> visited(rows, vector<bool>(cols, false));
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<>> heap;

        for (int row = 0; row < rows; ++row) {
            for (int col = 0; col < cols; ++col) {
                if (row == 0 || row == rows - 1 || col == 0 || col == cols - 1) {
                    heap.emplace(heightMap[row][col], row, col);
                    visited[row][col] = true;
                }
            }
        }

        const int directions[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int trapped = 0;

        while (!heap.empty()) {
            auto [height, row, col] = heap.top();
            heap.pop();

            for (const auto& direction : directions) {
                int nextRow = row + direction[0];
                int nextCol = col + direction[1];
                if (nextRow < 0 || nextRow >= rows || nextCol < 0 || nextCol >= cols || visited[nextRow][nextCol]) {
                    continue;
                }

                visited[nextRow][nextCol] = true;
                int nextHeight = heightMap[nextRow][nextCol];
                trapped += max(0, height - nextHeight);
                heap.emplace(max(height, nextHeight), nextRow, nextCol);
            }
        }

        return trapped;
    }
};
