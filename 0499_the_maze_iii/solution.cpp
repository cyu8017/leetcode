// LeetCode 0499 - The Maze III
// https://leetcode.com/problems/the-maze-iii/

#include <climits>
#include <queue>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

class Solution {
public:
    std::string findShortestWay(std::vector<std::vector<int>>& maze, std::vector<int>& ball,
                                std::vector<int>& hole) {
        const int rows = static_cast<int>(maze.size());
        const int cols = static_cast<int>(maze[0].size());
        const int holeRow = hole[0];
        const int holeCol = hole[1];
        const std::pair<int, int> directions[4] = {{1, 0}, {0, -1}, {0, 1}, {-1, 0}};
        const char labels[4] = {'d', 'l', 'r', 'u'};

        auto roll = [&](int row, int col, int dr, int dc) {
            int distance = 0;
            while (row + dr >= 0 && row + dr < rows && col + dc >= 0 && col + dc < cols &&
                   maze[row + dr][col + dc] == 0) {
                row += dr;
                col += dc;
                ++distance;
                if (row == holeRow && col == holeCol) {
                    break;
                }
            }
            return std::make_tuple(row, col, distance);
        };

        std::vector<std::vector<std::pair<int, std::string>>> best(
            rows, std::vector<std::pair<int, std::string>>(cols, {INT_MAX, ""}));
        using State = std::tuple<int, std::string, int, int>;
        std::priority_queue<State, std::vector<State>, std::greater<State>> heap;
        heap.emplace(0, "", ball[0], ball[1]);

        while (!heap.empty()) {
            auto [dist, path, row, col] = heap.top();
            heap.pop();
            if (best[row][col] <= std::make_pair(dist, path)) {
                continue;
            }
            best[row][col] = {dist, path};
            if (row == holeRow && col == holeCol) {
                return path;
            }

            for (int index = 0; index < 4; ++index) {
                const auto [dr, dc] = directions[index];
                const auto [nextRow, nextCol, traveled] = roll(row, col, dr, dc);
                if (nextRow == row && nextCol == col) {
                    continue;
                }
                const int newDist = dist + traveled;
                const std::string newPath = path + labels[index];
                const auto candidate = std::make_pair(newDist, newPath);
                if (candidate < best[nextRow][nextCol]) {
                    heap.emplace(newDist, newPath, nextRow, nextCol);
                }
            }
        }
        return "impossible";
    }
};
