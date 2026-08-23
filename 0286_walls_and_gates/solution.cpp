// LeetCode 0286 - Walls and Gates
// https://leetcode.com/problems/walls-and-gates/

#include <climits>
#include <queue>
#include <vector>

class Solution {
public:
    void wallsAndGates(std::vector<std::vector<int>>& rooms) {
        if (rooms.empty() || rooms[0].empty()) {
            return;
        }

        int rows = static_cast<int>(rooms.size());
        int cols = static_cast<int>(rooms[0].size());
        std::queue<std::pair<int, int>> queue;

        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (rooms[row][col] == 0) {
                    queue.push({row, col});
                }
            }
        }

        const int directions[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!queue.empty()) {
            auto [row, col] = queue.front();
            queue.pop();
            for (const auto& direction : directions) {
                int nextRow = row + direction[0];
                int nextCol = col + direction[1];
                if (nextRow >= 0 && nextRow < rows && nextCol >= 0 && nextCol < cols &&
                    rooms[nextRow][nextCol] == INT_MAX) {
                    rooms[nextRow][nextCol] = rooms[row][col] + 1;
                    queue.push({nextRow, nextCol});
                }
            }
        }
    }
};
