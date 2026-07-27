// LeetCode 1036 - Escape a Large Maze
// https://leetcode.com/problems/escape-a-large-maze/

#include <queue>
#include <unordered_set>
#include <utility>
#include <vector>

class Solution {
    static long long pack(int r, int c) { return (static_cast<long long>(r) << 20) | c; }

public:
    bool isEscapePossible(std::vector<std::vector<int>>& blocked, std::vector<int>& source,
                          std::vector<int>& target) {
        std::unordered_set<long long> blockedSet;
        for (auto& b : blocked) blockedSet.insert(pack(b[0], b[1]));
        int B = static_cast<int>(blocked.size());
        int limit = B * (B - 1) / 2;

        auto bfs = [&](const std::vector<int>& start, const std::vector<int>& goal) {
            std::queue<std::pair<int, int>> q;
            std::unordered_set<long long> seen;
            q.push({start[0], start[1]});
            seen.insert(pack(start[0], start[1]));
            const int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
            while (!q.empty()) {
                if (static_cast<int>(seen.size()) > limit) return true;
                auto [r, c] = q.front();
                q.pop();
                if (r == goal[0] && c == goal[1]) return true;
                for (auto& d : dirs) {
                    int nr = r + d[0], nc = c + d[1];
                    if (nr < 0 || nr >= 1000000 || nc < 0 || nc >= 1000000) continue;
                    long long k = pack(nr, nc);
                    if (blockedSet.count(k) || seen.count(k)) continue;
                    seen.insert(k);
                    q.push({nr, nc});
                }
            }
            return false;
        };

        return bfs(source, target) && bfs(target, source);
    }
};

