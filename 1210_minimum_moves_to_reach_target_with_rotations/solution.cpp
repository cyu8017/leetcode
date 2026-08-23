// LeetCode 1210 - Minimum Moves to Reach Target with Rotations
// https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/

#include <queue>
#include <set>
#include <tuple>
#include <vector>

class Solution {
public:
    int minimumMoves(std::vector<std::vector<int>>& grid) {
        const int n = static_cast<int>(grid.size());
        using State = std::tuple<int, int, int>;
        State start{0, 0, 0};
        State target{n - 1, n - 2, 0};
        std::queue<std::pair<State, int>> q;
        std::set<State> seen;
        q.push({start, 0});
        seen.insert(start);
        while (!q.empty()) {
            auto [state, moves] = q.front();
            q.pop();
            if (state == target) {
                return moves;
            }
            auto [r, c, orient] = state;
            std::vector<State> nxt;
            if (orient == 0) {
                if (c + 2 < n && grid[r][c + 2] == 0) {
                    nxt.push_back({r, c + 1, 0});
                }
                if (r + 1 < n && grid[r + 1][c] == 0 && grid[r + 1][c + 1] == 0) {
                    nxt.push_back({r + 1, c, 0});
                    nxt.push_back({r, c, 1});
                }
            } else {
                if (r + 2 < n && grid[r + 2][c] == 0) {
                    nxt.push_back({r + 1, c, 1});
                }
                if (c + 1 < n && grid[r][c + 1] == 0 && grid[r + 1][c + 1] == 0) {
                    nxt.push_back({r, c + 1, 1});
                    nxt.push_back({r, c, 0});
                }
            }
            for (const auto& ns : nxt) {
                if (!seen.count(ns)) {
                    seen.insert(ns);
                    q.push({ns, moves + 1});
                }
            }
        }
        return -1;
    }
};
