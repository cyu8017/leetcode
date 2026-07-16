// LeetCode 0317 - Shortest Distance from All Buildings
// https://leetcode.com/problems/shortest-distance-from-all-buildings/

#include <algorithm>
#include <climits>
#include <deque>
#include <vector>

class Solution {
public:
    int shortestDistance(std::vector<std::vector<int>>& grid) {
        if (grid.empty()) {
            return -1;
        }

        int rows = static_cast<int>(grid.size());
        int cols = static_cast<int>(grid[0].size());
        int buildings = 0;
        std::vector<std::vector<int>> distances(rows, std::vector<int>(cols, 0));
        std::vector<std::vector<int>> reach(rows, std::vector<int>(cols, 0));
        const int directions[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        for (const std::vector<int>& row : grid) {
            for (int cell : row) {
                if (cell == 1) {
                    buildings += 1;
                }
            }
        }

        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (grid[row][col] != 1) {
                    continue;
                }
                std::deque<std::vector<int>> queue;
                std::vector<std::vector<bool>> visited(rows, std::vector<bool>(cols, false));
                queue.push_back({row, col, 0});
                visited[row][col] = true;
                while (!queue.empty()) {
                    std::vector<int> current = queue.front();
                    queue.pop_front();
                    int currentRow = current[0];
                    int currentCol = current[1];
                    int distance = current[2];
                    for (const auto& direction : directions) {
                        int nextRow = currentRow + direction[0];
                        int nextCol = currentCol + direction[1];
                        if (nextRow >= 0 && nextRow < rows && nextCol >= 0 && nextCol < cols
                            && grid[nextRow][nextCol] == 0 && !visited[nextRow][nextCol]) {
                            visited[nextRow][nextCol] = true;
                            distances[nextRow][nextCol] += distance + 1;
                            reach[nextRow][nextCol] += 1;
                            queue.push_back({nextRow, nextCol, distance + 1});
                        }
                    }
                }
            }
        }

        int best = INT_MAX;
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (grid[row][col] == 0 && reach[row][col] == buildings) {
                    best = std::min(best, distances[row][col]);
                }
            }
        }

        return best == INT_MAX ? -1 : best;
    }
};
