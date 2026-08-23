// LeetCode 1263 - Minimum Moves to Move a Box to Their Target Location
// https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/

#include <queue>
#include <set>
#include <string>
#include <utility>
#include <vector>

class Solution {
public:
    int minPushBox(std::vector<std::vector<char>>& grid) {
        const int m = static_cast<int>(grid.size());
        const int n = static_cast<int>(grid[0].size());
        std::pair<int, int> box, player, target;
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (grid[r][c] == 'B') {
                    box = {r, c};
                } else if (grid[r][c] == 'S') {
                    player = {r, c};
                } else if (grid[r][c] == 'T') {
                    target = {r, c};
                }
            }
        }
        auto reachable = [&](std::pair<int, int> start, std::pair<int, int> blocked) {
            std::set<std::pair<int, int>> seen{start};
            std::vector<std::pair<int, int>> stack{start};
            static const int dr[] = {1, -1, 0, 0};
            static const int dc[] = {0, 0, 1, -1};
            while (!stack.empty()) {
                auto [r, c] = stack.back();
                stack.pop_back();
                for (int i = 0; i < 4; ++i) {
                    std::pair<int, int> nxt{r + dr[i], c + dc[i]};
                    if (nxt.first >= 0 && nxt.first < m && nxt.second >= 0 && nxt.second < n &&
                        grid[nxt.first][nxt.second] != '#' && nxt != blocked && !seen.count(nxt)) {
                        seen.insert(nxt);
                        stack.push_back(nxt);
                    }
                }
            }
            return seen;
        };
        using State = std::pair<std::pair<int, int>, std::pair<int, int>>;
        std::queue<std::tuple<std::pair<int, int>, std::pair<int, int>, int>> q;
        std::set<State> seen;
        q.push({box, player, 0});
        seen.insert({box, player});
        static const int dr[] = {1, -1, 0, 0};
        static const int dc[] = {0, 0, 1, -1};
        while (!q.empty()) {
            auto [b, p, pushes] = q.front();
            q.pop();
            if (b == target) {
                return pushes;
            }
            auto canReach = reachable(p, b);
            for (int i = 0; i < 4; ++i) {
                std::pair<int, int> stand{b.first - dr[i], b.second - dc[i]};
                std::pair<int, int> nb{b.first + dr[i], b.second + dc[i]};
                if (canReach.count(stand) && nb.first >= 0 && nb.first < m && nb.second >= 0 && nb.second < n &&
                    grid[nb.first][nb.second] != '#') {
                    State state{nb, b};
                    if (!seen.count(state)) {
                        seen.insert(state);
                        q.push({nb, b, pushes + 1});
                    }
                }
            }
        }
        return -1;
    }
};
