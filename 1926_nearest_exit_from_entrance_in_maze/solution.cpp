// LeetCode 1926 - Nearest Exit from Entrance in Maze
// https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

#include <queue>
#include <tuple>
#include <vector>

class Solution {
public:
    int nearestExit(std::vector<std::vector<char>>& maze, std::vector<int>& entrance) {
        int m = (int)maze.size(), n = (int)maze[0].size();
        int er = entrance[0], ec = entrance[1];
        std::queue<std::tuple<int, int, int>> q;
        q.emplace(er, ec, 0);
        maze[er][ec] = '+';
        static const int D[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!q.empty()) {
            auto [r, c, d] = q.front();
            q.pop();
            for (auto& dir : D) {
                int nr = r + dir[0], nc = c + dir[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && maze[nr][nc] == '.') {
                    if (nr == 0 || nr == m - 1 || nc == 0 || nc == n - 1) return d + 1;
                    maze[nr][nc] = '+';
                    q.emplace(nr, nc, d + 1);
                }
            }
        }
        return -1;
    }
};
