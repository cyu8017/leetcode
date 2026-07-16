// LeetCode 0490 - The Maze
// https://leetcode.com/problems/the-maze/

#include <set>
#include <utility>
#include <vector>

class Solution {
public:
    bool hasPath(std::vector<std::vector<int>>& maze, std::vector<int>& start, std::vector<int>& destination) {
        const int rows = static_cast<int>(maze.size());
        const int cols = static_cast<int>(maze[0].size());
        const int directions[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        std::set<std::pair<int, int>> visited;
        std::vector<std::pair<int, int>> stack = {{start[0], start[1]}};

        while (!stack.empty()) {
            const auto [row, col] = stack.back();
            stack.pop_back();
            if (visited.count({row, col}) > 0) {
                continue;
            }
            visited.insert({row, col});
            if (row == destination[0] && col == destination[1]) {
                return true;
            }
            for (const auto& direction : directions) {
                int nextRow = row;
                int nextCol = col;
                while (nextRow + direction[0] >= 0 && nextRow + direction[0] < rows &&
                       nextCol + direction[1] >= 0 && nextCol + direction[1] < cols &&
                       maze[nextRow + direction[0]][nextCol + direction[1]] == 0) {
                    nextRow += direction[0];
                    nextCol += direction[1];
                }
                if (visited.count({nextRow, nextCol}) == 0) {
                    stack.emplace_back(nextRow, nextCol);
                }
            }
        }
        return false;
    }
};
