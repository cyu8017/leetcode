// LeetCode 0542 - 01 Matrix
// https://leetcode.com/problems/01-matrix/

#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> updateMatrix(std::vector<std::vector<int>>& mat) {
        const int rows = static_cast<int>(mat.size());
        const int cols = static_cast<int>(mat[0].size());
        const int inf = 1'000'000'000;
        std::vector<std::vector<int>> dist(rows, std::vector<int>(cols, inf));
        std::queue<std::pair<int, int>> queue;

        for (int row = 0; row < rows; ++row) {
            for (int col = 0; col < cols; ++col) {
                if (mat[row][col] == 0) {
                    dist[row][col] = 0;
                    queue.emplace(row, col);
                }
            }
        }

        const int directions[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!queue.empty()) {
            const auto [row, col] = queue.front();
            queue.pop();
            for (const auto& direction : directions) {
                const int nextRow = row + direction[0];
                const int nextCol = col + direction[1];
                if (nextRow >= 0 && nextRow < rows && nextCol >= 0 && nextCol < cols &&
                    dist[nextRow][nextCol] > dist[row][col] + 1) {
                    dist[nextRow][nextCol] = dist[row][col] + 1;
                    queue.emplace(nextRow, nextCol);
                }
            }
        }

        return dist;
    }
};
