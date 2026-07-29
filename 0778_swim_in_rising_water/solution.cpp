// LeetCode 0778 - Swim in Rising Water
// https://leetcode.com/problems/swim-in-rising-water/

#include <algorithm>
#include <queue>
#include <tuple>
#include <vector>

class Solution {
public:
    int swimInWater(std::vector<std::vector<int>>& grid) {
        int n = static_cast<int>(grid.size());
        using Node = std::tuple<int, int, int>;
        std::priority_queue<Node, std::vector<Node>, std::greater<Node>> heap;
        std::vector<std::vector<bool>> seen(n, std::vector<bool>(n, false));
        heap.push({grid[0][0], 0, 0});
        seen[0][0] = true;
        static const int dirs[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        while (!heap.empty()) {
            auto [time, r, c] = heap.top();
            heap.pop();
            if (r == n - 1 && c == n - 1) {
                return time;
            }
            for (auto& d : dirs) {
                int nr = r + d[0];
                int nc = c + d[1];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && !seen[nr][nc]) {
                    seen[nr][nc] = true;
                    heap.push({std::max(time, grid[nr][nc]), nr, nc});
                }
            }
        }
        return -1;
    }
};
