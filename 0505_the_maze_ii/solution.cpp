// LeetCode 0505 - The Maze II
// https://leetcode.com/problems/the-maze-ii/

#include <climits>
#include <queue>
#include <tuple>
#include <utility>
#include <vector>

class Solution {
public:
    int shortestDistance(std::vector<std::vector<int>>& maze, std::vector<int>& start,
                         std::vector<int>& destination) {
        const int rows = static_cast<int>(maze.size());
        const int cols = static_cast<int>(maze[0].size());
        const int targetRow = destination[0];
        const int targetCol = destination[1];
        const std::pair<int, int> directions[4] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        std::vector<std::vector<int>> best(rows, std::vector<int>(cols, INT_MAX));
        using State = std::tuple<int, int, int>;
        std::priority_queue<State, std::vector<State>, std::greater<State>> heap;
        heap.emplace(0, start[0], start[1]);

        while (!heap.empty()) {
            auto [dist, row, col] = heap.top();
            heap.pop();
            if (row == targetRow && col == targetCol) {
                return dist;
            }
            if (best[row][col] <= dist) {
                continue;
            }
            best[row][col] = dist;

            for (const auto& [dr, dc] : directions) {
                int nextRow = row;
                int nextCol = col;
                int traveled = 0;
                while (nextRow + dr >= 0 && nextRow + dr < rows && nextCol + dc >= 0 &&
                       nextCol + dc < cols && maze[nextRow + dr][nextCol + dc] == 0) {
                    nextRow += dr;
                    nextCol += dc;
                    ++traveled;
                }
                if (nextRow == row && nextCol == col) {
                    continue;
                }
                const int newDist = dist + traveled;
                if (newDist < best[nextRow][nextCol]) {
                    heap.emplace(newDist, nextRow, nextCol);
                }
            }
        }
        return -1;
    }
};
